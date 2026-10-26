profit = 100000
loss = -30000

success_probability = 0.8
failure_probability = 0.2

expected_value = (profit * success_probability) + (loss * failure_probability)

print("Decision Tree")
print("----------------------------")
print("            Start")
print("              |")
print("        Launch Product")
print("         /          \\")
print(f"Success ({success_probability*100:.0f}%)   Failure ({failure_probability*100:.0f}%)")
print(f"Profit = {profit}      Loss = {loss}")

print("\nExpected Value =", expected_value)

if expected_value > 0:
    print("Decision: Launch the Product")
else:
    print("Decision: Do Not Launch the Product")
