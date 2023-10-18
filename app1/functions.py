FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """
    Read a text file and return the list of to-do items.
    """
    with open(file_path, "r") as file_local:  # use context manager
        todos_local = file_local.readlines()  # closes the file automatically, thus recommended over the file.close()
    return todos_local


def write_todos(write_file, file_path=FILEPATH):
    """
    Write a to-do items list in a text file.
    """
    with open(file_path, "w") as file_local:
        file_local.writelines(write_file)
    return None


if __name__ == "__main__":
    print("Hello")