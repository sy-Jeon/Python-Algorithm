'''
Parenthesis String (PS) consists of two parenthesis symbols ‘(’ and ‘)’ only. In parenthesis strings, some strings are called a valid PS (shortly, VPS).
Let us give the formal definition of VPS. A single “( )” is a member of VPS, called the base VPS.
Let x and y be a member of VPS. Then “(x)”, a VPS which encloses a VPS x with a single pair of parenthesis, is also a member of VPS.
And xy, the concatenation of two VPS x and y, is a member of VPS. For example, “(())()” and ((()))” are all VPS, but “(()(”, “(())()))” and “(()” are not VPS.
You are given a set of PS. You should decide if the input string is VPS or not. 

Info.
Your program is to read from standard input.
The input consists of T test cases.
The number of test cases T is given in the first line of the input.
Then PS’s are given in the following T lines one by one.
The length of each PS is between 2 and 50, inclusively.
'''

t = int(input())

for i in range(t):
    command = list(input())
    sum = 0

    for j in range(len(command)):
        if command[j] == "(":
            sum += 1
        else:
            sum -= 1

        if sum < 0: # ())일 때
            print("NO")
            break

    if sum > 0:     # 짝 개수가 맞지 않을 떄
        print("NO")
    elif sum == 0:  # 짝 개수가 똑같을 때
        print("YES")