# ------------------------------------------------------------------------------------------------ #
#                                   Files, Directories and Paths                                   #
# ------------------------------------------------------------------------------------------------ #

### Openining a file in the same folder
file = open("day_24/my_file.txt", mode="r")


### Reading a file
contents = file.read()
print(contents)


### Closing a file
# - Why is it important to close the file?
# -- It takes up resources on computer; closing it will save resources
file.close()


### Opening a file with the the 'with' keyword
# -- Opening files with the 'with' automatically handles the closing of files
with open("day_24/my_file.txt", mode="w") as file:
    file.write("\nNew Text.")


### Relative vs Absolute File Paths
# - Root Folder --> the main folder of all files (Macintosh HD in MacOS, C: in Windows)

### Absolute File Paths
# - Absolute File Paths are ALWAYS relative to the root
# -- Examples
# --- / --> the root
# --- /Work --> the Work folder inside of root
# --- /Work/report.doc --> the report.doc file inside of the Work folder inside of the root


### Relative File Paths
# - Relative File Paths are ALWATS relative to the current working directory
# - Relative paths use single dots (./) to go into a child folder
# - Relative Paths use double dots (../) to go up to a parent folder
# -- Examples
# --- ./report.doc --> working in the same directory and accessing the report.doc file

### Differences between windows and Mac
# - File paths in Mac use /
# - File paths in Windows use \
# - In python, it doesn't matter, use /


### Example: Importing from a different directory
with open("/Users/marlonnunez/Desktop/my_file.text", mode="w") as file:
    file.write("\nNew Text.")
