# find even or odd

def main():
    number = int(input("Number: "))
    if paritycheck(number):
        n = "Even"
    else:
        n= "Odd"
    print(n)

def paritycheck(num):
    # if num%2!=0:
    #     return "Odd"
    # else:
    #     return "Even"
    # return True if num%2==0 else False
    return num%2==0

if __name__== "__main__":
    main()