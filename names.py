name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# names = []

# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)
    
# for name in sorted(names):
#     print(f"hello, {name}")