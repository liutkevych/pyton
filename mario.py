def main():
    print_square(3)

def print_square(size):
    # For each row in a square
    for i in range(size):
        # For each break in a row
        for y in range(size):
            # Print brick
            print("#", end="")
        # go to a new row
        print()
main()