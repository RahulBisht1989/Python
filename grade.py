score = int(input("Score: "))
limit=100

if score>limit:
    print("Score can't be more than 100")
    exit()

if score>=90:
    grade = "A"
elif score>=80:
    grade = "B"
elif score>=70:
    grade = "C"
elif score>=60:
    grade = "D"
else:
    grade = "E"

print(f"You scored {score}, Grade: {grade}")
