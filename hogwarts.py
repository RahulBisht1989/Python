#students = ["Rahul","Bobby","Shetal","Anaysha","Shivu"]

# # for student in students:
# #     print(student)

# for i in range(len(students)):
#     print(students[i])

students = [
    {
        "name":"Rahul",
        "house":"Panther",
        "id":7687
    },
    {
        "name":"Bobby",
        "house":"hippopotamus",
        "id": 787
    }
]

for student in students:
    print(f"my name is {student['name']} , my house is {student['house']} and badge number is {student['id']}")