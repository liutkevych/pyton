students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"}, 
    {"name": "Ron", "house": "Gryffindor"}, 
    {"name": "Draco", "house": "Slytherin"}, 
]


def is_griffyndor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_griffyndor, students)

for griffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(griffindor["name"])