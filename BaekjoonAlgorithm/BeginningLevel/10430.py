n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

print((n1 + n2) % n3)
print(((n1 % n3) + (n2 % n3)) % n3)
print((n1 * n2) % n3)
print(((n1 % n3) * (n2 % n3)) % n3)
