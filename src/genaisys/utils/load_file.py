def load_file(file_path) -> str:
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        text = "Error: File not found. Please check the file path."
    return text