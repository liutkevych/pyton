# List and  Distionary
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}, 
    {"name": "Ron", "house": "Gryffindor", "patronus": "Djack Rassel terrier"}, 
    {"name": "Draco", "house": "Slytherin", "patronus": None}, 
]

# When we use for loop for dictionary than we iterate through the keys of the dictionary
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")