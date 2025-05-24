from langchain.tools import tool
import os


# Tool 1: List contents of the current directory
@tool
def list_directory_contents() -> str:
    """List all files and directories in the current working directory.
    
    Returns:
        str: A string containing the list of files and directories, or an error message.
    """
    try:
        cwd = os.getcwd()
        items = os.listdir(cwd)
        if not items:
            return "The current directory is empty."
        return "\n".join(items)
    except Exception as e:
        return f"Error accessing directory: {str(e)}"

# Tool 2: Write content to a Markdown file (from previous response)
@tool
def write_markdown_file(content: str, filename: str) -> str:
    """Write content to a Markdown file in the current working directory.
    
    Args:
        content (str): The content to write to the Markdown file.
        filename (str): The name of the Markdown file (e.g., 'test_doc2.md').
    
    Returns:
        str: A message indicating success or failure.
    """
    try:
        if not filename.endswith('.md'):
            filename += '.md'
        cwd = os.getcwd()
        file_path = os.path.join(cwd, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully wrote content to {file_path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"
