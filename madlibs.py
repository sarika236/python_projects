# string concatenation (aka how to put string together)
# suppose we want to create a string that says "subscribe to ______"

#youtuber = "sarika chaturvedi" # some string variable

# a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("varb: ")
verb2 = input("verb: ")
famous_person = input("Famous person: ")
madlib = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)