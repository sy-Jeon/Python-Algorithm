import math
 
def solve():
    n = int(input())
    # list start from 0 so, put anything number
    arr = [0, 0, 1, 1]
   
    for i in range(4, n+1):
        # arr[i-1]: If number is 5, first of all you have to -1 from 5
        one, two, three = math.inf, math.inf, arr[i-1]
    
        if i % 3 == 0:
            one = arr[i//3]
      
        if i % 2 == 0:
            two = arr[i//2]
        # 1. If number is 5, first of all you have to -1 from 5. -> (1 + min(?, ?, ?))
        # 2. And then number 4's arr value is 2 -> (1 + 2)
        value = 1 + min(one, two, three)     
        arr.append(value)

    print(value)
    
solve()
