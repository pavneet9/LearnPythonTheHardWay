# read a file in python

from sys import argv

script, filename = argv
print(filename)
txt = open( filename )
print txt.read()

print "\n \n"
filename1 = raw_input(" \n \n Enter the File Again")
txt = open( filename1 )
print txt.read()
