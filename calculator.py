# importing oprtstor to prtform mathematical operations
from operator import pow, truediv, mul, add, sub  
import time



operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv
}

#main function
def calculate_main(input_string):
    if input_string.isdigit():
        return float(input_string)
    for c in operators.keys():
        left, operator, right = input_string.partition(c)
        if operator in operators:
            return operators[operator](calculate_main(left), calculate_main(right))

calc = input()
print("Answer: " + str(calculate_main(calc)))

time.sleep(20)