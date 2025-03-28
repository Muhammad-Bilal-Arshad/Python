# types of files
#  text files: .txt, .docx, .log etc
# binary files: .mp4, .mov, .png, .jpeg etc


# file opening

# f = open('filename','mode')

# filename is file name whereas mode is read or write denoted by r or w
# data = f.read() reading all the data from the opened file
#

#f.close() to close the file


with open("sample.txt", "r") as file: # for reading
    content = file.read()
    print(content)  # Displays file content
    file.close()

# for writing, it overwrites every existing thing
with open("sample.txt", "w") as file:
    file.write("New data!")
    file.close()

# for appending , basically adding to existing data

with open("sample.txt", "a") as file:
    file.write("\nAppending new line!")
    file.close()

# read and write mode, modify without clearing

with open("sample.txt", "r+") as file:
    print(file.read())  # Read first
    file.seek(0)  # Move cursor to the beginning
    file.write("Hey!")  # Modify part of the file
    file.seek(0)
    print(file.read())  # Read again
    file.close()
# read and write mode, clears before writing

with open("sample.txt", "w+") as file:
    file.write("Fresh content!\n")
    file.seek(0)  # Move back to read
    print(file.read())
    file.close()

