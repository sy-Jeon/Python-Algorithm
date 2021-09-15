hex = int(input(), 16)

for n in range(1, 16):
    a = hex * n
    print('%X'%hex, '*', '%X'%n, '=', '%X'%a, sep="")