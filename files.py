# Files.py

print "We are going to delete the file you mention"

filename = raw_input("?")
file = open(filename, 'w')
file.truncate()

# Let's write something into the file

line1 = "This is the first line"
line2 = "Hey we got another file"

# Let's write these lines into a file

file.write(line1)
file.write('\n')
file.write(line2)

#close the file
file.close()
