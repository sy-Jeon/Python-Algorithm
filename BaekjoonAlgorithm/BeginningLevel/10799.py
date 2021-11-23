bar_laser = list(input())
result = 0
stack = []

for i in range(len(bar_laser)):
    if bar_laser[i] == '(':
        stack.append('(')
        
    else:
        if bar_laser[i-1] == '(':
            stack.pop()
            result += len(stack)
            
        else:
            stack.pop() 
            result += 1

print(result)
