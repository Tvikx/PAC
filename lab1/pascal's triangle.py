import argparse
from math import *

parser = argparse.ArgumentParser(description = 'number of lines')
parser.add_argument('height', type = int, help = 'plz write number of lines')
args = parser.parse_args()

def print_triangle(N):
    for i in range(N):
        for j in range(N - i + 1):
            print(end = " ")
        for j in range(i + 1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end = " ")
        print()
    pass

print_triangle(args.height)
