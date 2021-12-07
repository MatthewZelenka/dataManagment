import math
import numpy as np
import functools as ft

#Permutations unit
def factorial(num = int):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

def permutation(n = int, r = int): #number of ways to arrage objects
    return factorial(n)/factorial(n-r)

def permutationIdenticals(n = int, r = int, identicals = list): #number of ways to arrage objects with identical items
    product = 1
    for x in identicals:
        product = product*factorial(x)
    return permutation(n, r)/product

#Combinations unit
def union(setA = list, setB = list):
    setC = []
    for item in setA:
        setC.append(item)
    for item in setB:
        if item not in setC:
            setC.append(item)
    return setC

def intersection(setA = list, setB = list):
    setC = []
    for item in setB:
        if item in setA:
            setC.append(item)
    return setC

def compliment(universalSet = list, setA = list):
    setB = []
    for item in universalSet:
        if item not in setA:
            setB.append(item)
    return setB

def combination(n = int, r = int):
    #return permutation(n, r)/factorial(r)
    return factorial(n)/(factorial(n-r)*factorial(r))

def binomialTheorem():
    return "WIP"

#Statistics of One Variable unit

#Central Tendencys
def mean(num_list):
    return sum(num_list)/len(num_list)

def median(num_list):
    num_list.sort()
    return (num_list[math.floor((len(num_list)+1)/2)-1]+num_list[math.ceil((len(num_list)+1)/2)-1])/2 #sorts number and finds the value of the middle of the list

def mode(num_list):
    table = []
    for item in num_list: #creates a table with all the values with the frequency
        if not table:
            table.append([item, 1])
        elif item in [value[0] for value in table]:
            table[[value[0] for value in table].index(item)][1] = table[[value[0] for value in table].index(item)][1]+1
        else:
            table.append([item, 1])
    table.sort(key=lambda elem: elem[1], reverse=True) #sorts table by frequency
    mode = []
    max_frequency = table[0][1] #sets max frequency as first frequency the list as it was just sorted
    for frequency in [value[1] for value in table]: #finds all other values with the same frequency
        if frequency == max_frequency:
            mode.append(table[[value[1] for value in table].index(frequency)][0])
            table.pop(table.index(table[[value[1] for value in table].index(frequency)]))
    return sorted(mode)

#Data analysis
def analysis(num_list): #finds range suggest range of intervel based on intervel amout if added in 
    return
def stem_leaf(num_list):
    table = []
    for item in num_list: #creates a table with all the values with the stems tehn finds the leafs for each nunber and catogorise them
        if not table:
            table.append([math.floor(item/10), [item%10]])
        elif math.floor(item/10) in [value[0] for value in table]:
            table[[value[0] for value in table].index(math.floor(item/10))][1].append(item%10)
        else:
            table.append([math.floor(item/10), [item%10]])
    table.sort(key=lambda elem: elem[0], reverse=False) #sorts table by stem from lowest to highest
    return table
def organize(num_list, start=0, intervel_length=1, include="[)"): #gets starting number and then gets intervel range and sorts list
    table = []
    for _ in range(math.ceil(max(num_list)/intervel_length)):
        table
        if not table:
            table.append([[include[0], start, start+intervel_length, include[1]], []])
        else:
            table.append([[include[0], table[-1][0][2], table[-1][0][2]+intervel_length, include[1]], []])
    for sort in range(len(table)):
        for num in num_list:
            if ((table[sort][0][0] == "(" and num > table[sort][0][1]) or (table[sort][0][0] == "[" and num >= table[sort][0][1])) and ((table[sort][0][3] == ")" and num < table[sort][0][2]) or (table[sort][0][3] == "]" and num <= table[sort][0][2])):
                table[sort][1].append(num)
    return table
def frequency(num_list, start=0, intervel_length=1, include="[)"):
    table = organize(num_list, start=start, intervel_length=intervel_length, include=include)
    for sort in range(len(table)):
        table[sort][1] = len(table[sort][1])
    return table
def cumulative_frequency(num_list, start=0, intervel_length=1, include="[)"):
    table = frequency(num_list, start=start, intervel_length=intervel_length, include=include)
    for sort in range(len(table)-1):
        table[sort+1][1] = table[sort+1][1]+table[sort][1]
    return table
def relative_frequency(num_list, start=0, intervel_length=1, include="[)"):
    table = organize(num_list, start=start, intervel_length=intervel_length, include=include)
    for sort in range(len(table)):
        table[sort][1] = len(table[sort][1])/len(num_list)
    return table

#Measures of spread
def range_from_start(num_list, parts, part_num):
    return (num_list[math.floor((len(num_list)+1)*part_num/parts)-1]+num_list[math.ceil((len(num_list)+1)*part_num/parts)-1])/2 #finds the number at an interval for a preset amount of groups

class quartiles():
    @staticmethod
    def Q1(num_list): #finds the number at the 1st interval out of 4
        return range_from_start(num_list=num_list, parts=4, part_num=1)
    @staticmethod
    def Q2(num_list): #finds the number at the 2nd interval out of 4
        return median(num_list)
    @staticmethod
    def Q3(num_list): #finds the number at the 3rd interval out of 4
        return range_from_start(num_list=num_list, parts=4, part_num=3)
    @staticmethod
    def IQR(num_list): #subtracts Q3 from Q1
        return quartiles.Q3(num_list)-quartiles.Q1(num_list)
    @staticmethod
    def SIQR(num_list): #divides IQR by 2
        return quartiles.IQR(num_list)/2
    @staticmethod
    def all(num_list): #returns all of functions in the quartiles class
        return {"Q1":quartiles.Q1(num_list), "Q2":quartiles.Q2(num_list), "Q3":quartiles.Q3(num_list), "IQR":quartiles.IQR(num_list), "SIQR":quartiles.SIQR(num_list)}

def outliers(num_list): #finds outlier by checking all the numbers to see if they are greater then Q3+1.5*IQR or less then Q1-1.5*IQR
    outliers = []
    for num in num_list:
        if num > quartiles.Q3(num_list)+1.5*quartiles.IQR(num_list) or num < quartiles.Q1(num_list)-1.5*quartiles.IQR(num_list):
            outliers.append(num)
    return outliers

def box_and_whisker(num_list, modified = False): #Outputs min, Q1, median, Q3, max and outliers if told to remove
    numbers = []
    for num in num_list:
        if modified == True and num not in outliers(num_list):
            numbers.append(num)
        elif modified == False:
            numbers.append(num)
    plot = {"min":min(numbers), "Q1":quartiles.Q1(num_list), "median":median(num_list), "Q3":quartiles.Q3(num_list), "max":max(numbers)}
    if modified == True:
        plot.update({"outliers":outliers(num_list)})
    return plot

def precentile(num_list, precent): #find the number at precent out of 100%
    return range_from_start(num_list=num_list, parts=100, part_num=precent)

class  variance():
    @staticmethod
    def sample(num_list, variance=False): #calculates variance for sample
        MEAN = mean(num_list)
        i = 0
        for num in num_list:
            i = i+pow((num-MEAN), 2)
        return i/(len(num_list)-1)
    @staticmethod
    def population(num_list, variance=False): #calculates variance for population
        MEAN = mean(num_list)
        i = 0
        for num in num_list:
            i = i+pow((num-MEAN), 2)
        return i/(len(num_list))

class standerd_deviation():
    @staticmethod
    def sample(num_list): #calculates standerd deviation for sample
        return math.sqrt(variance.sample(num_list))
    @staticmethod
    def population(num_list): #calculates standerd deviation for population
        return math.sqrt(variance.population(num_list))

#Statistics of Two Variables unit

def matrix_multiplier(array0, array1):
    return np.matmul(array0, array1)

def inverse_matrix(array):
    return np.linalg.inv(array)

def regression(numList, maxPower=1):
    if maxPower < 1:
        return ("Error term count must be greater then 1")
    maxPower = round(maxPower)
    array0 = [[sum([i[0]**((maxPower-term)+(maxPower-level)) for i in numList]) for term in range(maxPower+1)] for level in range(maxPower+1)]
    array1 = [[sum([(j[0]**(maxPower-term))*(j[1]) for j in numList])] for term in range(maxPower+1)]
    answerKey = matrix_multiplier(inverse_matrix(array0), array1)
    return answerKey
    
def coefficientOfDetermination(numList, answerKey, r2=True):
    COD = (1-(sum(([(i[1]-(sum([(answerKey[term]*i[0]**(len(answerKey)-1-term))for term in range(len(answerKey))])))**2 for i in numList]))/sum(([(i[1]-sum([i[1] for i in numList])/len([i[1] for i in numList]))**2 for i in numList]))))[0]
    return COD if r2 == True else math.sqrt(COD)
    
    
def equationMaker(answerKey, scientificNotation=False):
    equation = "y="
    for i in range(len(answerKey)):
        equation = "%s%s%s"%(
            equation, 
            "" if i==0 or 0 > answerKey[i] else "+" ,
            (str(answerKey[i][0]) if scientificNotation == False else "({:e})".format(answerKey[i][0]))) + ("x" if i != len(answerKey)-1 else "") + ("^%d"%(len(answerKey)-1-i) if i < len(answerKey)-2 else ""
        )
    return equation

#Probability
def oddToProbability(odd = str):
    nums = [float(i) for i in odd.split(':')]
    return nums[0]/(nums[0]+nums[1])

def float_gcd(a, b, rtol = 1e-05, atol = 1e-08):
    t = min(abs(a), abs(b))
    while abs(b) > rtol * t + atol:
        a, b = b, a % b
    return a

def probabilityToOdd(probability = int):
    nums = [probability,1-probability]
    denominater = float_gcd(nums[0], nums[1])
    return f"{nums[0]/denominater}:{nums[1]/denominater}"

#Distributions
def probabilityDistributionExpectedValue(ValuesAndPX = [[1,1]]):
    return sum([XAndP[0]*XAndP[1] for XAndP in ValuesAndPX])

def bernoulliTrial(numOfTrials, numOfSuccesses, decimalOfSuccsses, orderMatters=False):
    return (combination(numOfTrials, numOfSuccesses) if orderMatters == False else 1)*(decimalOfSuccsses**numOfSuccesses)*((1-decimalOfSuccsses)**(numOfTrials-numOfSuccesses))

def bernoulliTrialExpectedValue(numOfTrials, decimalOfSuccsses):
    return numOfTrials*decimalOfSuccsses

def geometicDistribution(numOfTrialsBeforeSuccsses, decimalOfSuccsses):
    return ((1-decimalOfSuccsses)**numOfTrialsBeforeSuccsses)*decimalOfSuccsses

def geometicDistributionExpectedValue(decimalOfSuccsses):
    return (1-decimalOfSuccsses)/decimalOfSuccsses

def hypergeometicDistribution(numOfSuccsses, numOfSuccssesChosen, totalNumOfItems, totalNumOfItemsChosen): # a x n r
    return (combination(numOfSuccsses, numOfSuccssesChosen)*combination(totalNumOfItems-numOfSuccsses, totalNumOfItemsChosen-numOfSuccssesChosen))/(combination(totalNumOfItems, totalNumOfItemsChosen))

def hypergeometicDistributionExpectedValue(numOfSuccsses, totalNumOfItems, totalNumOfItemsChosen):
    return (totalNumOfItemsChosen*numOfSuccsses)/totalNumOfItems