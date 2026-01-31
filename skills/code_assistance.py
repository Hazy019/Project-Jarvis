import os

def read_project_file(filename):
    """Reads a file from the current directory and returns its content."""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                content = f.read()
            return content
        else:
            return f"Sir, I cannot locate the file named {filename} in the workspace."
    except Exception as e:
        return f"An error occurred while accessing the data: {e}"