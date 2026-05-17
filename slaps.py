import random
slaps = range(10)

name = input("What is your name? \n")

s= random.choices(slaps)

print(f"{name},hmmm you get {s} slap")