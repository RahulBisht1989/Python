# import random
# house = ["Gryffindor","Slytherin","Ravenclaw","Hufflepuff"]

name = input("whats your name: ").title()
# assignedhouse = random.choice(house)
# print(f"hmmm...{name}, you are {assignedhouse}")

match name:
    case "Rahul"|"Bobby"|"Meena":
        print("RED")
    case "Sheetal":
        print("Yellow")
    case "Anaysha":
        print("Pink")
    case "Shivansh":
        print("Blue")
    case _:
        print("?")
