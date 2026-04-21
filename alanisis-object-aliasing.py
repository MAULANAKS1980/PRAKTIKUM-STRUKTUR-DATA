a = [1, 2, 3]
b = a  # aliasing

print("Sebelum perubahan:")
print("a:", a)
print("b:", b)

b.append(4)

print("\nSetelah b.append(4):")
print("a:", a)
print("b:", b)