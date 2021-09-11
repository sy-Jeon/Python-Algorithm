n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)
result = (n1 if n1 < n2 else n2) if n1 < n3 else (n3 if n3 < n2 else n2)
print(result)