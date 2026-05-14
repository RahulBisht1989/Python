def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    sum = add_numbers(a,b)
    print("The sum is:", sum)


def add_numbers(x, y):
    return x + y

main()
