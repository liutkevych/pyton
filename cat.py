def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("How many times to meow? "))
        if n > 0:
            return n


main()
    
