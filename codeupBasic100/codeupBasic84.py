hertz, bit, channel, second = input().split()
hertz, bit, channel, second = int(hertz), int(bit), int(channel), int(second)
dbstorage = hertz * bit * channel * second / 8 / 1024 / 1024
print(format(dbstorage, "0.1f"), "MB")