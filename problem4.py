import os

def list_directory_contents(directory_path):
    try:
        entries = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.")
    except OSError as e:
        print(f"OS error occurred: {e}")

if __name__ == "__main__":
    path = '/'
    if not path:
        path = os.getcwd()
    list_directory_contents(path)
