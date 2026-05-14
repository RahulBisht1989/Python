import random
slaps = [3,0,6,1,10,15,100,2,8,0]

name = input("What is your name? \n")

s= random.choices(slaps)

print(f"{name},hmmm you get {s} slap")
