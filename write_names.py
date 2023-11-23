import csv
name = input("What's your name? ")
city = input("In which city do you live? ")

with open("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "city"])
    writer.writerow({"name": name, "city": city})