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

r= 1000000

check = [True for _ in range(r)]

for i in range(2,int(r**0.5)+1):
    if check[i]==True:
        for j in range(i*2, r, i) : 
            if check[j] == True :
                check[j] = False            #에라토스테네스의 체
