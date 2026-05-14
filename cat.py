# meow = int(input("how many should a cat meow: "))
# for _ in range(meow):
#     print("meow")
# count = 0

# while count<meow:
#     print("meow")
#     count+=1

# print("meow\n" * 3, end="")

# while True:
#     meow = int(input("how many should a cat meow: "))
#     if meow>0 and type(meow)== int:
#         break

# for _ in range(meow):
#     print("meow")

def main():
    n = get_number()
    meow(n)

def get_number():
    while True:
        n = int(input("what is n: "))
        if n>0:
            return n       
    
def meow(n): 
    for _ in range(n):
        print("Meow")
    

if __name__=="__main__":
    main()
