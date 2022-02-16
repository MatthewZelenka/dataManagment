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

regresionPowerList = {
    0, 1, 2, 3
}

for maxPower in regresionPowerList:
    answerKey = regression(Values, maxPower=maxPower)
    print("Regression for power of %d: %s" % (maxPower, equationMaker(answerKey, scientificNotation=False)))
    print("R%s value is: %s" % ("^2" if maxPower > 1 else "", coefficientOfDetermination(Values, answerKey, r2=True if maxPower > 1 else False)))