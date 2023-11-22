def main():
    # Ask user to put his name
    name = input("Type your name, please \n")
    output = hello(name)
    print(output)

def hello(to="world"):
    # Remove whitespases and capitalize user's name
    to = to.strip().title()
    # Say hello to user
    return f"Hello, {to}"

if __name__ == "__main__":
    main()