import matplotlib.pyplot as plt

salaries = [25000, 28000, 30000, 32000, 35000,
            38000, 40000, 42000, 45000, 48000,
            50000, 52000, 55000, 60000, 65000]

plt.figure(figsize=(6, 4))
plt.hist(salaries, bins=5)
plt.title("Histogram of Employee Salaries")
plt.xlabel("Salary (Rs.)")
plt.ylabel("Number of Employees")
plt.show()

plt.figure(figsize=(6, 4))
plt.boxplot(salaries)
plt.title("Box Plot of Employee Salaries")
plt.ylabel("Salary (Rs.)")
plt.show()
