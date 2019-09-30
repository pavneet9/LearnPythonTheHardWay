#First functions in python

def print_args(*args):
    args1, args2 = args
    print "lets print the first %s and the second arg %s" %(args1, args2)

def print_args1(args1, args2):
    print "lets print the first %s and the second arg %s" %(args1, args2)

def print_args2(args1):
    print "lets print the first %s" %(args1)

def print_args3(args2):
        print "lets print the second arg %s" %(args2)

print_args("Pavneet", "Singh")
print_args1("Pavneet", "Singh")
print_args2("Singh")
print_args3("Singh")
