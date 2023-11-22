while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x should be a number!")
    else:
        break
   
print(f"x is {x}")