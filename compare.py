a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a < b:
    message = (f"{a} is less than {b}")
elif a > b:
    message = (f"{a} is greater than {b}")
else:
    message = (f"{a} is equal to {b}")

if a<b or a>b:
    print(f"{a} is not equal to {b}")

print(message)