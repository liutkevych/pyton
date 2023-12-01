import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="Number of times to meow", type=int)
arrgs = parser.parse_args()

for _ in range(arrgs.n):
    print("meow")