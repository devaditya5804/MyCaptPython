#Question 2:
def get_file_extension(filename):
    # Split the filename into its base name and extension
    split_filename = filename.split(".")
    
    # Check if there is an extension
    if len(split_filename) > 1:
        # Return the last element of the split, which is the extension
        return split_filename[-1]
    else:
        # If there is no extension, return an empty string
        return ""

def language_name(extension):
    language_dict = {
        "py": "Python",
        "java": "Java",
        "cpp": "C++",
        "js": "JavaScript",
        # Add more extensions and language mappings as needed
    }
    
    # Lookup the extension in the language dictionary
    if extension in language_dict:
        return language_dict[extension]
    else:
        return "Unknown"

# Get the filename from the user
filename = input("Enter a filename: ")

# Get the extension of the filename
extension = get_file_extension(filename)

# Get the language name associated with the extension
language = language_name(extension)

# Print the extension and language name
if extension:
    print(" extension of the file is:", extension)
    print("file is coded in:", language)
else:
    print("The file has no extension.")
