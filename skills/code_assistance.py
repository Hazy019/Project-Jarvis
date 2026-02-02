import os


def read_project_file(filename=None, max_chars=20000):
    """If `filename` is given, read that file; otherwise scan workspace .py files and return combined content.

    Limits output to `max_chars` characters for performance.
    """
    try:
        if filename:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                    return f.read()
            return f"I cannot locate the file named {filename} in the workspace."

        # Scan for python files in workspace
        collected = []
        total = 0
        for root, dirs, files in os.walk('.'):
            # skip virtual environments or hidden folders
            if any(part.startswith('.') or part.lower().startswith('venv') for part in root.split(os.sep)):
                continue
            for fname in files:
                if fname.endswith('.py'):
                    path = os.path.join(root, fname)
                    try:
                        with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
                            data = fh.read()
                        # trim if adding would exceed max
                        allowed = max_chars - total
                        if allowed <= 0:
                            break
                        if len(data) > allowed:
                            data = data[:allowed]
                        collected.append(f"# FILE: {path}\n" + data)
                        total += len(data)
                    except Exception:
                        continue
            if total >= max_chars:
                break

        if not collected:
            return "No python files found in workspace."
        return "\n\n".join(collected)

    except Exception as e:
        return f"An error occurred while scanning the project: {e}"