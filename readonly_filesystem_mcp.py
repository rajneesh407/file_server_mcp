import os
import glob
import mimetypes
from pathlib import Path
from typing import List, Optional
from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger

# Initialize logger
logger = get_logger(__name__)

# Initialize FastMCP server
mcp = FastMCP("Read-Only File System MCP")

# Configuration
DEFAULT_ROOT_PATH = os.path.join(os.getcwd(), "uploads")
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB limit for reading files
ALLOWED_EXTENSIONS = {
    ".txt",
    ".py",
    ".js",
    ".html",
    ".css",
    ".json",
    ".xml",
    ".md",
    ".csv",
    ".log",
}


def is_safe_path(base_path: str, path: str) -> bool:
    """Check if the path is safe and within the allowed directory."""
    try:
        base_path = os.path.abspath(base_path)
        full_path = os.path.abspath(path)
        return full_path.startswith(base_path)
    except (OSError, ValueError):
        return False


def get_file_info(file_path: str) -> dict:
    """Get basic information about a file."""
    try:
        stat = os.stat(file_path)
        mime_type, _ = mimetypes.guess_type(file_path)
        return {
            "name": os.path.basename(file_path),
            "path": file_path,
            "size": stat.st_size,
            "modified": stat.st_mtime,
            "mime_type": mime_type or "unknown",
            "is_file": os.path.isfile(file_path),
            "is_directory": os.path.isdir(file_path),
        }
    except (OSError, ValueError) as e:
        return {"error": str(e)}


@mcp.tool(
    description="List files and directories in a given path. Only shows files within the allowed directory."
)
def list_directory(path: str = ".") -> str:
    """List contents of a directory."""
    try:
        # Ensure path is within allowed directory
        if not is_safe_path(DEFAULT_ROOT_PATH, path):
            return f"Error: Path '{path}' is outside the allowed directory '{DEFAULT_ROOT_PATH}'"

        if not os.path.exists(path):
            return f"Error: Path '{path}' does not exist"

        if not os.path.isdir(path):
            return f"Error: '{path}' is not a directory"

        items = []
        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
            info = get_file_info(item_path)
            if "error" not in info:
                item_type = "DIR" if info["is_directory"] else "FILE"
                size_str = f"{info['size']} bytes" if info["is_file"] else ""
                items.append(f"{item_type:4} {item:<30} {size_str}")

        if not items:
            return f"Directory '{path}' is empty"

        return f"Contents of '{path}':\n" + "\n".join(items)

    except Exception as e:
        return f"Error listing directory: {str(e)}"


@mcp.tool(
    description="Read the contents of a text file. Only reads files with safe extensions and within size limits."
)
def read_file(file_path: str, max_lines: int = 100) -> str:
    """Read contents of a text file."""
    try:
        # Ensure path is within allowed directory
        if not is_safe_path(DEFAULT_ROOT_PATH, file_path):
            return f"Error: Path '{file_path}' is outside the allowed directory '{DEFAULT_ROOT_PATH}'"

        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' does not exist"

        if not os.path.isfile(file_path):
            return f"Error: '{file_path}' is not a file"

        # Check file size
        file_size = os.path.getsize(file_path)
        if file_size > MAX_FILE_SIZE:
            return f"Error: File '{file_path}' is too large ({file_size} bytes). Maximum allowed size is {MAX_FILE_SIZE} bytes."

        # Check file extension
        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext not in ALLOWED_EXTENSIONS:
            return f"Error: File type '{file_ext}' is not allowed. Allowed extensions: {', '.join(ALLOWED_EXTENSIONS)}"

        # Read file content
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        total_lines = len(lines)
        if total_lines > max_lines:
            content = "".join(lines[:max_lines])
            content += (
                f"\n... (showing first {max_lines} lines of {total_lines} total lines)"
            )
        else:
            content = "".join(lines)

        return f"File: {file_path}\nSize: {file_size} bytes\nLines: {total_lines}\n\nContent:\n{content}"

    except Exception as e:
        return f"Error reading file: {str(e)}"


@mcp.tool(
    description="Search for files by name pattern in a directory and its subdirectories."
)
def find_files(pattern: str, directory: str = ".") -> str:
    """Find files matching a pattern."""
    try:
        # Ensure directory is within allowed path
        if not is_safe_path(DEFAULT_ROOT_PATH, directory):
            return f"Error: Directory '{directory}' is outside the allowed directory '{DEFAULT_ROOT_PATH}'"

        if not os.path.exists(directory):
            return f"Error: Directory '{directory}' does not exist"

        if not os.path.isdir(directory):
            return f"Error: '{directory}' is not a directory"

        # Search for files
        search_pattern = os.path.join(directory, "**", pattern)
        matches = glob.glob(search_pattern, recursive=True)

        # Filter to only include files (not directories)
        files = [f for f in matches if os.path.isfile(f)]

        if not files:
            return f"No files found matching pattern '{pattern}' in '{directory}'"

        # Get file info for each match
        results = []
        for file_path in files:
            info = get_file_info(file_path)
            if "error" not in info:
                results.append(
                    f"{info['name']:<30} {info['size']:>8} bytes  {file_path}"
                )

        return f"Found {len(files)} files matching '{pattern}':\n" + "\n".join(results)

    except Exception as e:
        return f"Error searching files: {str(e)}"


@mcp.tool(description="Search for text content within files in a directory.")
def search_in_files(
    search_text: str, directory: str = ".", file_pattern: str = "*"
) -> str:
    """Search for text content within files."""
    try:
        # Ensure directory is within allowed path
        if not is_safe_path(DEFAULT_ROOT_PATH, directory):
            return f"Error: Directory '{directory}' is outside the allowed directory '{DEFAULT_ROOT_PATH}'"

        if not os.path.exists(directory):
            return f"Error: Directory '{directory}' does not exist"

        if not os.path.isdir(directory):
            return f"Error: '{directory}' is not a directory"

        # Find files matching pattern
        search_pattern = os.path.join(directory, "**", file_pattern)
        files = [
            f for f in glob.glob(search_pattern, recursive=True) if os.path.isfile(f)
        ]

        # Filter by allowed extensions
        files = [
            f for f in files if os.path.splitext(f)[1].lower() in ALLOWED_EXTENSIONS
        ]

        matches = []
        for file_path in files:
            try:
                # Check file size before reading
                if os.path.getsize(file_path) > MAX_FILE_SIZE:
                    continue

                with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                    lines = f.readlines()

                # Search for text in lines
                for line_num, line in enumerate(lines, 1):
                    if search_text.lower() in line.lower():
                        matches.append(f"{file_path}:{line_num}: {line.strip()}")

            except Exception as e:
                continue  # Skip files that can't be read

        if not matches:
            return f"No matches found for '{search_text}' in files matching '{file_pattern}'"

        return f"Found {len(matches)} matches for '{search_text}':\n" + "\n".join(
            matches[:50]
        )  # Limit to 50 matches

    except Exception as e:
        return f"Error searching in files: {str(e)}"


@mcp.tool(
    description="Get information about a file or directory (size, type, permissions, etc.)."
)
def get_file_info_tool(file_path: str) -> str:
    """Get detailed information about a file or directory."""
    try:
        # Ensure path is within allowed directory
        if not is_safe_path(DEFAULT_ROOT_PATH, file_path):
            return f"Error: Path '{file_path}' is outside the allowed directory '{DEFAULT_ROOT_PATH}'"

        if not os.path.exists(file_path):
            return f"Error: Path '{file_path}' does not exist"

        info = get_file_info(file_path)
        if "error" in info:
            return f"Error getting file info: {info['error']}"

        # Format the information
        result = f"File Information for: {file_path}\n"
        result += f"Name: {info['name']}\n"
        result += f"Type: {'Directory' if info['is_directory'] else 'File'}\n"
        result += f"Size: {info['size']} bytes\n"
        result += f"MIME Type: {info['mime_type']}\n"
        result += f"Modified: {info['modified']}\n"

        return result

    except Exception as e:
        return f"Error getting file info: {str(e)}"


@mcp.tool(description="Get the current working directory and available space.")
def get_directory_info() -> str:
    """Get information about the current directory and available space."""
    try:
        import shutil

        # Get current directory
        current_dir = os.getcwd()

        # Get available space
        total, used, free = shutil.disk_usage(current_dir)

        # Get allowed root directory info
        root_info = f"Allowed root directory: {DEFAULT_ROOT_PATH}\n"
        root_info += f"Root exists: {os.path.exists(DEFAULT_ROOT_PATH)}\n"

        if os.path.exists(DEFAULT_ROOT_PATH):
            root_total, root_used, root_free = shutil.disk_usage(DEFAULT_ROOT_PATH)
            root_info += f"Root free space: {root_free // (1024**3)} GB\n"

        return f"""Directory Information:
Current directory: {current_dir}
Free space: {free // (1024**3)} GB
Total space: {total // (1024**3)} GB
Used space: {used // (1024**3)} GB

{root_info}

Configuration:
Max file size: {MAX_FILE_SIZE // (1024**2)} MB
Allowed extensions: {', '.join(ALLOWED_EXTENSIONS)}"""

    except Exception as e:
        return f"Error getting directory info: {str(e)}"


def main():
    """Main function to run the read-only file system MCP server."""
    logger.info("Starting Read-Only File System MCP Server")
    logger.info(f"Root directory: {DEFAULT_ROOT_PATH}")
    logger.info(f"Max file size: {MAX_FILE_SIZE // (1024**2)} MB")
    logger.info(f"Allowed extensions: {', '.join(ALLOWED_EXTENSIONS)}")

    # Run the MCP server over HTTP on localhost port 8080
    mcp.run(transport="http", host="localhost", port=8080)


if __name__ == "__main__":
    main()
