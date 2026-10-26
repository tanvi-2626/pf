import hashlib

result = hashlib.md5(b'Priya')
result1 = hashlib.md5(b'Rajak')

print("The byte equivalent of hash(Priya):", end="")
print(result.digest())

print("The byte equivalent of hash(Rajak) :", end="")
print(result1.digest())
