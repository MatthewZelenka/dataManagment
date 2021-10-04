from Data_Managment import *
from datetime import datetime
startTime = datetime.now()

Values = [102.947639, 112.779789, 119.427375, 132.668593, 145.300179, 169.662804, 173.768556, 195.920075, 231.033361, 265.657385, 308.661929, 350.287848, 399.162311, 453.425806, 534.161529, 616.242094, 674.360382, 758.937825, 860.294365, 917.762612, 975.503216, 1087.728205, 1256.147371, 1447.809875, 1652.916985, 1852.781899, 2052.428714, 2257.847343, 2440.003049, 2643.161035, 2909.533494, 3198.891771, 3523.483224, 3925.520688, 4412.919867, 5039.10345, 5821.210961, 6793.052193, 7555.032225, 8287.678054, 9231.648126, 10275.25569, 11169.93553, 11894.48419, 12517.20043, 12946.66674, 13532.91518, 14306.39612]
print("Values:", sorted(Values),"\n") #numbers
print("Mean:", mean(Values)) #from central_tendencys
print("Median:", median(Values))
print("Mode:", mode(Values),"\n")
print("Q1:", quartiles.Q1(Values)) #from measures_of_spread
print("Q2:", quartiles.Q2(Values))
print("Q3:", quartiles.Q3(Values))
print("IQR:", quartiles.IQR(Values))
print("SIQR:", quartiles.SIQR(Values))
print("All:", quartiles.all(Values),"\n")
print("Outliers:", outliers(Values))
per = 70;print(per, "precentile:", precentile(Values, per))
print("Box and wisker plot:", box_and_whisker(Values))
print("Box and wisker plot(modified):", box_and_whisker(Values, modified=True),"\n")
print("Standard deviation(sample):", standerd_deviation.sample(Values))
print("Variance(sample):", variance.sample(Values))
print("Standard deviation(population):", standerd_deviation.population(Values))
print("Variance(population):", variance.population(Values),"\n")
print("Stem and leaf:", stem_leaf(Values),"\n")
start_value = 0; intervel_length=10; include="(]"
print("Starting value: %d\nIntervel length: %d\nInclued: %s\n" %(start_value, intervel_length, include))
print("Organize:", organize(Values, start=start_value, intervel_length=intervel_length, include=include),"\n") #from data_analysis
print("Frequency:", frequency(Values, start=start_value, intervel_length=intervel_length, include=include),"\n")
print("Cumulative Frequency:", cumulative_frequency(Values, start=start_value, intervel_length=intervel_length, include=include),"\n")
print("Relative Frequency:", relative_frequency(Values, start=start_value, intervel_length=intervel_length, include=include),"\n")

print("Compleation time:",datetime.now() - startTime)