import argparse 
import io
import sys

parser = argparse.ArgumentParser(description = 'Path to the matrix file')
parser.add_argument('PATH', type = str, help = 'type path to the file with matrices')
args = parser.parse_args()

def check_input():
    """this function checks the correctness of the input data"""

    input_file = open(args.PATH, 'r', encoding = 'utf-8')
    for line in input_file:
        line.split()
        if(line.isdigit() or ' '): continue
        else:
            print(f"{line}inccorect input: matrices should contain only digits\n")
            sys.exit(1)
    input_file.close
    
def read_matrix(input):
    """this function opens input file and gets matrix"""

    matrix = []
    for row in input:
        if(row != '\n'):
            arr = [float(t) for t in row.split()]
            matrix.append(arr)
        else: 
            break
    return matrix

def check_matrices(matrix1, matrix2):
    """this function checks the correctness of the matrices"""

    if(len(matrix1[0]) != len(matrix2)):
        print('incorrect matrix size\nYou must use matrices NxM MxK\n')
        sys.exit(1)

def matr_mult(matrix1, matrix2):
    """this function multiply two matrices"""

    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix2)] for row_a in matrix1]
    return result


def print_result(res):
    """this function prints the result"""

    output = open('output.txt', 'w', encoding = 'utf-8')
    output.write('\n'.join('\t'.join(map(str, row)) for row in res))



check_input()
input_file = open(args.PATH, 'r', encoding = 'utf-8')
matrix1 = read_matrix(input_file)
matrix2 = read_matrix(input_file)
check_matrices(matrix1, matrix2)
input_file.close()
res = matr_mult(matrix1, matrix2)
print_result(res)




