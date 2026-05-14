name = input("Whats your name? ").title().strip()
while True:
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
        print("Please enter a valid number for age.")
city =input("Where do you live? ").title().strip()

print("Hello,", name+"!")
print("You are", age, "years old.")
print("You live in", city + ".") 

abc = False
while True:
    try:
        float_number = input("Enter a floating-point number: ")
        float_number = float(float_number)
        print("You entered the floating-point number:", float_number)
        abc = True
        print("Flag: ", abc)
        break
    except ValueError:
        print("That's not a valid floating-point number.")


print("Flag after loop: ", abc)

