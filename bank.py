balance = 0

def main():
    print("balance:", balance)
    deposit(100)
    withdrow(50)
    print("balance:", balance)

def deposit(n):
    global balance
    balance += n

def withdrow(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()