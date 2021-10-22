from dataManagment import *

fact = 1
print(f"Factorial of {fact}:", factorial(fact))
n1 = 11 #total amount of things that can be arranged (default = 1)
r1 = 4 #amount of things you want arranged out if the total (default = 1)
print(f"Permutation of P({n1}, {r1}):", permutation(n1, r1))

n2 = 11 #total amount of things that can be arranged (default = 1)
r2 = n2 #amount of things you want arranged out if the total (default = n2)
identicals = [2,2] #total amount of diffrent identical things you you have (default = 1)
print(f"Permutation of P({n1}, {r1}) with these identicals {identicals}):", permutationIdenticals(n2, r2, identicals))