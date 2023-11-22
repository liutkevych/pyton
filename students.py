import csv

students = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row['name'], "city": row['city']})

for student in sorted(students, key=lambda student: student['city'], reverse=True):
    print(f"{student['name']} lives in {student['city']}")



# with open("names.csv") as file:
#     for line in file:
#         name, city = line.rstrip().split(",")
#         print(f"{name} lives in {city}")