import numpy as np

np.random.seed(10)

n = int(input("Enter the number of samples: "))

normal_data = np.random.normal(loc=50, scale=10, size=n)
uniform_data = np.random.uniform(low=0, high=100, size=n)
exponential_data = np.random.exponential(scale=5, size=n)

def analyze(data, name):
    print("\n" + "=" * 45)
    print(name)
    print("=" * 45)
    print("Generated Values:")
    print(np.round(data, 2))
    print("Mean               :", round(np.mean(data), 2))
    print("Minimum Value      :", round(np.min(data), 2))
    print("Maximum Value      :", round(np.max(data), 2))
    print("Standard Deviation :", round(np.std(data), 2))

analyze(normal_data, "Normal Distribution")
analyze(uniform_data, "Uniform Distribution")
analyze(exponential_data, "Exponential Distribution")
