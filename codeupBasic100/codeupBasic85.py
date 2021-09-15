height, width, bit = input().split()
height, width, bit = int(height), int(width), int(bit)
dbstorage = height * width * bit / 8 / 1024 / 1024
print(format(dbstorage, "0.2f"), "MB")