import sys
import io


class Accountant:

    def __init__(self) -> None:
        pass

    def get_worker_salary(self, worker):
        if(isinstance(worker, Worker)):
            print(f"{type(worker).__name__}'s salary: {worker._salary}\n")
            return worker._salary
        
    def set_worker_salary(self, worker, new_salary):
        if(isinstance(new_salary, int) and new_salary > 0 and isinstance(worker, Worker)):
            worker._salary = new_salary
            print(f"{type(worker).__name__}'s new salary: {worker._salary}\n")
            pass

    def give_salary(self, worker):
        if(isinstance(worker, Worker)):
            worker._take_salary(worker._salary)
            print(f"{type(worker).__name__}'s got paid: {worker._salary}\n")
            pass
    
            
class Worker:
    def __init__(self, salary, cash = 0):
        Worker._cash = cash
        Worker._salary = salary

    @property
    def cash(self):
        print(f"{type(self).__name__}'s cash: {self._cash}\n")
        return self._cash
    
    def _take_salary(self, salary):
        self._cash += self._salary
        return self
    
    def _do_work(self, fileName1, fileName2):
        print(f"{type(self).__name__}'s work result is:\n")
        self.do_work(fileName1, fileName2)

    def _read_matrix(self, inputf):
        """this function opens input file and gets matrix"""

        input = open(inputf, 'r', encoding = 'utf-8')
        matrix = []
        for row in input:
            if(row != '\n'):
                arr = [float(t) for t in row.split()]
                matrix.append(arr)
            else: 
                break
        return matrix
    
    def _print_matr(self, matrix):
        for r in matrix:
            print(r)
        print("\n")
        
    def _check_input(self, input):
        """this function checks the correctness of the input data"""

        input_file = open(input, 'r', encoding = 'utf-8')
        for line in input_file:
            line.split()
            if(line.isdigit() or ' '): continue
            else:
                print(f"{line}inccorect input: matrices should contain only digits\n")
                sys.exit(1)
        input_file.close
    
    
class Pupa(Worker):
    def __init__(self, salary, cash=0):
        super().__init__(salary, cash)

    def do_work(self, fileName1, fileName2):
        self._check_input(fileName1)
        self._check_input(fileName2)
        matrix1 = self._read_matrix(fileName1)
        matrix2 = self._read_matrix(fileName2)
        result = [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))] 
        self._print_matr(result)

        
class Lupa(Worker):
    def __init__(self, salary, cash=0):
        super().__init__(salary, cash)
    
    def do_work(self, fileName1, fileName2):
        self._check_input(fileName1)
        self._check_input(fileName2)
        matrix1 = self._read_matrix(fileName1)
        matrix2 = self._read_matrix(fileName2)
        result = [[matrix1[i][j] - matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
        self._print_matr(result)