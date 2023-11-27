class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Lviv", "New York", "London", "Krakow"]:
            raise ValueError("House is unecceptable")
        self._house = house

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("What's name? ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()