# Python Input

from sys import argv

script , username = argv
prompt = '>'

print "Hey, %s , are you ready to play %s" %(script , username)
print "Are, you ready to play %s" %(username)
play = raw_input(prompt)

print ( "You are ready to play - %r" %play)
