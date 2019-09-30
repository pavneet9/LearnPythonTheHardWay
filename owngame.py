# Call classes between other classes

# Class engine
#goldroom = goldroom()



class abstractroom(object):
    def __init__(self):
        #self.start = start
        self.quips = ["dead" , "fully dead" , "You are dead"]

    def death(self):
       print quips[randint(0, len(quips) -1)]
       exit(1)



class princessroom(abstractroom):
        def activateroom(self):
              print "You meet the princess"
              print "What do you do"

              eat = raw_input(">")

              if eat == "eat her":
                  self.death
              elif eat == "not at her":
                  self.death
              elif eat == "give her cake":
                  return "gold_pot"



class goldroom(abstractroom):
        def activateroom(self):
            print "take the gold pot and leave"
            self.death

class engine(object):
   # Defines all th rooms the user can be in
   rooms ={
            'princessroom': princessroom(),
            'goldroom' : goldroom()
         }

   # string -> returns the class for that room
   def first_room(self, room):
       self.current_room = engine.rooms.get(room)
       return self.current_room
   def return_room(self, room):
       if room == "finished":
          exit(1)
       self.current_room = engine.rooms.get(room)
       return self.current_room


move = engine()
room = move.first_room("princessroom")
while True:
    next_room = room.activateroom()
    room = move.retrun_room("next_room")
# here we start the game in the starter class
