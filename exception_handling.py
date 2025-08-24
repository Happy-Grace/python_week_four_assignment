# Error Handling Lab 🧪: 
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

def read_file():
    filename = input("Enter file name(e.g doc_file.txt): ").strip()

    try:
        with open(f"python_week_four_assignment\\{filename}", "r") as file:
            # Reads file content and print
            # content = file.read()

            print(f"\nFILE CONTENTS: ")
            # print(content)
            for line in file:
                line = line.rstrip()
                print(line)
            print("")

    except FileNotFoundError:
        print(f"\nThe file `{filename}` does not exist.\n")

    except PermissionError:
        print(f"\nError: You do not have the permission to read `{filename}`.\n")

    except IOError as e:
        print(f"\nAn I/O error occured: `{e}`.")


read_file()


