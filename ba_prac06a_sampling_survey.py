import random
import statistics

population = {
    "Student1": 2, "Student2": 3, "Student3": 4, "Student4": 5,
    "Student5": 3, "Student6": 2, "Student7": 6, "Student8": 4,
    "Student9": 3, "Student10": 5, "Student11": 4, "Student12": 2,
    "Student13": 6, "Student14": 3, "Student15": 5, "Student16": 4,
    "Student17": 2, "Student18": 5, "Student19": 3, "Student20": 4
}

sample_students = random.sample(list(population.keys()), 8)

sample_data = [population[student] for student in sample_students]

sample_mean = statistics.mean(sample_data)
sample_std = statistics.stdev(sample_data)

print("----- SURVEY RESULTS -----")
print("Population Size:", len(population))
print("Sample Size:", len(sample_students))

print("\nSelected Students and Study Hours:")
for student in sample_students:
    print(student, ":", population[student], "hours")

print("\nSample Data:", sample_data)
print("Sample Mean:", round(sample_mean, 2), "hours")
print("Sample Standard Deviation:", round(sample_std, 2), "hours")
