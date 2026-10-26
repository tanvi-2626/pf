import statistics

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

mean = statistics.mean(marks)
median = statistics.median(marks)
variance = statistics.variance(marks)
std_dev = statistics.stdev(marks)
minimum = min(marks)
maximum = max(marks)

try:
    mode = statistics.mode(marks)
except statistics.StatisticsError:
    mode = "No unique mode"

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Variance =", variance)
print("Standard Deviation =", round(std_dev, 2))
print("Minimum =", minimum)
print("Maximum =", maximum)
