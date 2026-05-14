name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

age = 2026 - birth_year

if age > 18:
    is_adult = "True"
else:
    is_adult = "False"

print("User: " + name)
print("Age: " + str(age))
print("Adult: " + is_adult)

total = int(input("Enter total expense: "))
tax = total * 0.10

print("Tax is: "+ str(tax))