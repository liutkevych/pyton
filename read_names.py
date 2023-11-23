with open("names.txt", "r") as file:
    for line in file:
        print(f"hello, {line.rstrip()}")
   