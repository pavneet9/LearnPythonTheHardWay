# converting an old function we did into classes

from sys import exit
from random import randint

class Game(object):
    """docstring for ."""

    def __init__(self, start):
        self.start = start
        self.quips = ["dead" , "fully dead" , "You are dead"]

    def play(self):
        next = self.start

        while True:
           room = getattr(self, next)
           print " /n"
           next = room()


    def death(self):
       print quips[randint(0, len(quips) -1)]
       exit(1)

    def princess_lives_here(self):
        print "You meet the princess"
        print "What do you do"

        eat = raw_input(">")

        if eat == "eat her":
            return "death"
        elif eat == "not at her":
            return "death"
        elif eat == "give her cake":
            return "gold_pot"

    def gold_pot(self):
        print "take the gold pot and leave"
        return "death"



bear_hunt = Game("princess_lives_here")
bear_hunt.play()
