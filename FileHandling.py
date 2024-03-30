# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as f:
            f.write("This is line 1\n")
            f.write("12345\n")
            f.write("Another line with some text and numbers: 42\n")
        print("File created successfully.")
    except Exception as e:
        print("Error occurred while creating the file:", e)

# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as f:
            content = f.read()
            print("Contents of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to access the file.")
    except Exception as e:
        print("Error occurred while reading the file:", e)

# File Appending
def append_file():
    try:
        with open("my_file.txt", "a") as f:
            f.write("Appending line 1\n")
            f.write("67890\n")
            f.write("Another line appended: 99\n")
        print("Content appended to the file.")
    except Exception as e:
        print("Error occurred while appending to the file:", e)

if __name__ == "__main__":
    # File Creation
    create_file()

    # File Reading and Display
    read_file()

    # File Appending
    append_file()
