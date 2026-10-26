n = int(input("Enter the number of decision alternatives: "))

best_ev = float('-inf')
best_choice = ""

for i in range(n):
    print("\nDecision Alternative", i + 1)
    name = input("Enter alternative name: ")

    outcomes = int(input("Enter the number of possible outcomes: "))

    ev = 0

    for j in range(outcomes):
        payoff = float(input(f"Enter payoff for outcome {j + 1}: "))
        probability = float(input(f"Enter probability for outcome {j + 1}: "))
        ev += payoff * probability

    print(f"Expected Value of {name} = {ev:.2f}")

    if ev > best_ev:
        best_ev = ev
        best_choice = name

print("\n----- Result -----")
print("Best Decision Alternative:", best_choice)
print("Maximum Expected Value:", round(best_ev, 2))
