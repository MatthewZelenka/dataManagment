from dataManagment import *

universalSet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
setA = [1, 2, 3]
setB = [3, 4, 5]
print(f"Union of {setA} and {setB} is:", union(setA, setB))
print(f"Intersection of {setA} and {setB} is:", intersection(setA, setB))
print(f"Compliment of {setA} is:", compliment(universalSet, setA))
n = 5 #total amount of things that can be arranged (default = 1)
r = 4 #amount of things you want arranged out if the total??? (default = 1)
print(f"Combination of C({n}, {r}):", combination(n, r))
row = 1  
pos = 1
print(f"The value of row {row} and position {pos} of Pascal's Triangle is:", combination(row, pos))