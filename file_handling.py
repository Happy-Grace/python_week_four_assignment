import os

# File Read & Write Challenge 🖋️: 
# Create a program that reads a file and writes a modified version to a new file.



# Modifies file content to uppercase.
def modify_upper(content):
    return content.upper()

# Modifies file content to lowercase.
def modify_lower(content):
    return content.lower()


# Using an existing file called `input.txt`
def read_and_modify_file(input_file, output_file, modify_func):
    try:
        # Reads the input file.
        with open(f"python_week_four_assignment\\{input_file}", "r") as file1:
            # input_file_name = os.path.basename(input_file)
            file_content = file1.read()

        # Modifies the inout file.
        modified_content = modify_func(file_content)

        # Writes the modified file into a new file (output file).
        with open(f"python_week_four_assignment\\{output_file}", "w") as file2:
            # output_file_name = os.path.basename(output_file)
            file2.write(modified_content)

        # Successful Message
        print(f"The modified file `{output_file}` has been succesfully created.\n")

    except FileNotFoundError:
        print(f"Error: The file `{input_file}` does not exist.\n")
    except Exception as e:
        print(f"An error occurred: `{e}`.\n")

    
# Main Function (Where execution starts from).
def main():
    # Ask user for file names
    input_file = input("Enter the input file name(name is input.txt): ").strip()
    output_file = input("Enter output file name(e.g: output.txt): ").strip()
    
    print("")
    
    choice = ''
    while choice not in ["1", "2"]:
        print("Choose your file modification type.")
        print("1. Convert File to Uppercase.")
        print("2. Convert File to Lowercase.")

        print("")

        choice = input("Enter either 1 or 2(from the option above): ").strip()
        
    if choice == "1":
        modify_func = modify_upper

    else:
        modify_func = modify_lower

    read_and_modify_file(input_file, output_file, modify_func)


# Execute the Main Function
if __name__ == "__main__":
    main()
            
