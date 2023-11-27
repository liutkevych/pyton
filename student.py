class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Lviv", "New York", "London", "Krakow"]:
            raise ValueError("House is unecceptable")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🤦‍♂️"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🧚‍♀️"



def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("What's name? ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)
    # try:
    #     return Student(name, house)
    # except ValueError:
    #     print("You should put correct data")


if __name__ == "__main__":
    main()