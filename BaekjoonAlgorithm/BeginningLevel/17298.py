num_count = int(input())
nums = list(map(int, input().split()))

stack = []
answer = [-1] * num_count

for i in range(num_count):
    while stack and nums[stack[-1]] < nums[i] :
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)
