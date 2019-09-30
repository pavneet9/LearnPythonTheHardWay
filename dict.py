from sys import exit
from random import randint

def death():
   quips = ["dead" , "fully dead" , "You are dead"]
   print quips[randint(0, len(quips) -1)]
   exit(1)

def princess_lives_here():
    print "You meet the princess"
    print "What do you do"

    eat = raw_input(">")

    if eat == "eat her":
        return "death"
    elif eat == "not at her":
        return "death"
    elif eat == "give her cake":
        return "gold_pot"

def gold_pot():
    print "take the gold pot and leave"
    return "death"
rooms = {
           'death' : death,
           'princess_lives_here' : princess_lives_here,
           'gold_pot' : gold_pot,
        }

def runner(map, start):
    next = start

    while True:
       room = map[next]

       print " /n"
       next = room()

runner(rooms, "princess_lives_here")
