ten_things = "apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

extra_stuff = []

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff
print stuff.pop()
print stuff
extra_stuff.append(stuff.pop())
print extra_stuff

print ', '.join(stuff)
print '#'.join(stuff[3:5])
print ', Thing: '.join(stuff)