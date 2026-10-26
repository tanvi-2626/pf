import numpy as np

population = np.array([
    45, 50, 52, 55, 58, 60, 62, 65, 67, 70,
    72, 74, 75, 78, 80, 82, 85, 88, 90, 95
])

population_mean = np.mean(population)
population_std = np.std(population)

sample_size = 5
number_of_samples = 1000

sample_means = []

for i in range(number_of_samples):
    sample = np.random.choice(population, sample_size)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

sampling_mean = np.mean(sample_means)
sampling_std = np.std(sample_means)

standard_error = population_std / np.sqrt(sample_size)

print("----- Sampling and Sampling Distribution -----")
print("Population Size:", len(population))
print("Population Mean:", round(population_mean, 2))
print("Population Standard Deviation:", round(population_std, 2))

print("\nSample Size:", sample_size)
print("Number of Samples:", number_of_samples)

print("\n----- Sampling Distribution -----")
print("Mean of Sample Means:", round(sampling_mean, 2))
print("Standard Deviation of Sample Means:", round(sampling_std, 2))
print("Theoretical Standard Error:", round(standard_error, 2))

print("\nEstimated Population Mean:", round(sampling_mean, 2))
