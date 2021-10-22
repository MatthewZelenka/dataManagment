from dataManagment import *

Values =[
    (-3, -36),
    (-2, -12),
    (-1, -2),
    (0,0),
    (1,0),
    (2,4),
    (3,18)
]

print("Correlation coefficient:", correlation_coefficient(Values))
print("Linear Regression:", linear_regression(Values))
print("Quadratic Regression:", quadratic_regression(Values))
# print("Cubic Regression:", cubic_regression(Values))
print(regression(Values, termCount=4, scientificNotation=False))