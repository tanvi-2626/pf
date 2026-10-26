import random

n = int(input("Enter the number of dice rolls: "))

frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(n):
    roll = random.randint(1, 6)
    frequency[roll] += 1

print("\nResults of Dice Rolling:")
print("----------------------------")
print("Face\tFrequency\tProbability")

for face in range(1, 7):
    probability = frequency[face] / n
    print(face, "\t", frequency[face], "\t\t", round(probability, 4))
