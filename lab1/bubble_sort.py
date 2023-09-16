import argparse
import random
import numpy as np
parser = argparse.ArgumentParser(description='arr length')
parser.add_argument('length', type=int, help='length of sorted arr')
args = parser.parse_args()
arr = np.random.rand(args.length)



def bubble_sort(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(N - 1):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)
    pass

bubble_sort(arr)
