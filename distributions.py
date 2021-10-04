from Data_Managment import *

XAndProbabilityOfX = [
    [1000000, 1/2000000], 
    [25000, 1/2000000],
    [1000, 5/2000000],
]

print("Probability Distribution Expected Value:", probabilityDistributionExpectedValue(ValuesAndPX=XAndProbabilityOfX))
print("Bernoulli Trial:", bernoulliTrial(numOfTrials=200, numOfSuccesses=40, decimalOfSuccsses=.18, orderMatters=False))
print("Bernoulli Trial Expected Value:", bernoulliTrialExpectedValue(numOfTrials=20, decimalOfSuccsses=0.1))
print("Geometic Distribution:", geometicDistribution(numOfTrialsBeforeSuccsses=1, decimalOfSuccsses=1/2))
print("Geometic Distribution Expected Value:", geometicDistributionExpectedValue(decimalOfSuccsses=1/2))
print("Hypergeometic Distribution:", hypergeometicDistribution(numOfSuccsses = 520, numOfSuccssesChosen = 15, totalNumOfItems = 2000, totalNumOfItemsChosen = 125))
print("Hypergeometic Distribution Expected Value:", hypergeometicDistributionExpectedValue(numOfSuccsses = 4, totalNumOfItems = 11, totalNumOfItemsChosen = 4))