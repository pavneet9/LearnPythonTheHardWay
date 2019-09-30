# Getting started with classes

class account(object):
    def __init__(self):
        self.number = 0

    def add_number(self, number):
        self.number = self.number + number

    def name(self):
        print "I am an account"

a = account()
b = account()

a.name()
b.name()

a.add_number(5)

print a.number
