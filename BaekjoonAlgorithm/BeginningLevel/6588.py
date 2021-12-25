'''
n 1742, Christian Goldbach, a German amateur mathematician, sent a letter to Leonhard Euler in which he made the following conjecture:

Every even number greater than 4 can be written as the sum of two odd prime numbers.

For example:
8 = 3 + 5. Both 3 and 5 are odd prime numbers.
20 = 3 + 17 = 7 + 13.
42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23.
Today it is still unproven whether the conjecture is right. (Oh wait, I have the proof of course, but it is too long to write it on the margin of this page.)

Anyway, your task is now to verify Goldbach's conjecture for all even numbers less than a million.
'''

# r= 1000000

# check = [True for _ in range(r)]

# for i in range(2,int(r**0.6)):
#     if check[i]==True:
#         for j in range(i*2, r, i) : 
#             if check[j] == True :
#                 check[j] = False            #에라토스테네스의 체

# print(check)




#에라토스테네스의 체
total_n = 1000000
prime_check = [True for _ in range(total_n)]

for i in range(3, len(prime_check)+1):

    for j in range(2, int(total_n ** 0.5)+1):

        if i % j == 0:
            break

    else:
        prime_check[i] = False

print(prime_check)

print(int(1000000 ** 0.5)+1)

print(int(3 ** 0.5)+1)


# import sys

# while True:
#     n = sys.stdin.readline().strip('\n')

#     if not n:
#         break

#     if int(n) <= 4:
#         continue

#     # 8에서 5을 뽑아낸다.
#     for i in range(int(n)-1, -1, -1):
#         if int(n) % 2 != 0:
#             print(i)
#             break
