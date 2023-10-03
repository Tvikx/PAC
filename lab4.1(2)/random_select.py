import numpy as np
import numpy.random as rand
import sys
import argparse

parser = argparse.ArgumentParser(
    prog = 'random_select.py',
    description = 'mixes data from real and synthetic sources with the certain probability of receiving synthetic data')

parser.add_argument('RD', type = str, help = 'realData_FilePath')
parser.add_argument('SD', type = str, help = 'syntheticData_FilePath')
parser.add_argument('P', type = float, help = 'probability of receiving synthetic data (supports values belonging [0;1])')

args = parser.parse_args()

def check_probability():
    """DESCRIPTION: checks the correctness of the probability input"""
    try:
        if(args.P < 0 or args.P > 1):
            raise ValueError
    except ValueError:
        print("Probability must belonging to [0;1]")
        sys.exit(1)
    return args.P

def read_input():
    """DESCRIPTION: reads files with real and synthetic data and checks their correctness"""
    Rarr = []
    Sarr = []

    try:
        r = open(args.RD, 'r', encoding = 'utf-8')
        s = open(args.SD, 'r', encoding = 'utf-8')
        Rarr = r.readline()
        Sarr = s.readline()
        if not all (x.isdigit() or x.isspace() or x == '-' for x in Rarr):
            raise TypeError
        if not all (x.isdigit() or x.isspace() or x == '-' for x in Sarr):
            raise TypeError
    except OSError as err:
        print("OS error:", err)
        sys.exit(1)
    except TypeError:
        print("Data sets mustn't be empty and should contain onlly digits")
        sys.exit(1)

    R_dataSet = np.array([int(t) for t in Rarr.split()])
    S_dataSet = np.array([int(t) for t in Sarr.split()])

    if(len(R_dataSet) != len(S_dataSet)):
        print("size of data sets must be equal")
        sys.exit(1)
    
    print(f"sorce real data: {R_dataSet}")
    print(f"source synthetic data: {S_dataSet}")

    return R_dataSet, S_dataSet


def mix_arrays(R_dataSet, S_dataSet, p):
    """DESCRIPTION: mixes data sets with p probability """

    r = rand.rand(len(R_dataSet))                                                       #creates an array of numbers from 0 to 1
    mask = r > p                                                                        #creates a boolean array. An element becomes true if the value in r is more than the probability
    res = np.array(list(map(lambda x: not x, mask))) * S_dataSet + mask * R_dataSet     
    print(f"\nmixed with probability {p}:\n{res}")
    
def mix_arrays2(R_dataSet, S_dataSet, p):
    """DESCRIPTION: mix_arrays method 2"""
    
    r = rand.rand(len(R_dataSet))
    mask = r > p
    print(f"\nmixed with probability {p}:\n{np.where(mask, R_dataSet, S_dataSet)}")
    
def mix_arrays3(R_dataSet, S_dataSet, p):
    """DESCRIPTION: mix_arrays method 3"""
    
    r = rand.rand(len(R_dataSet))
    mask = r > p
    S_dataSet[mask] = R_dataSet[mask]
    print(f"\nmixed with probability {p}:\n{S_dataSet}")

    
    
p = check_probability()
R_dataSet, S_dataSet = read_input()
mix_arrays(R_dataSet, S_dataSet, p)
mix_arrays2(R_dataSet, S_dataSet, p)
mix_arrays3(R_dataSet, S_dataSet, p)