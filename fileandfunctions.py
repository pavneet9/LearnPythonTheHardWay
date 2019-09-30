from sys import argv

script, filename = argv

# Function to print everything in the file
def print_all(file):
    file.read()

# Function to print a line in the filename
def print_a_line(file, line_count):
    print line_count, file.readline()

# Function to seek a line
def rewind(file):
    file.seek(0)

file = open(filename)

#Print all the content of the file
print_all(file)
rewind(file)
# Print the line
current_line = 1
print_a_line(file,current_line)

current_line = current_line + 1
print_a_line(file,current_line)
