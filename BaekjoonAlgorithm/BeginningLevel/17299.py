from collections import Counter

n = int(input())
nums = list(map(int, input().split()))
counter = Counter(nums)
stack = []
ngf = [-1] * n

for i in range(n):
    # counter[nums[i]]의 경우, i가 6일 때 nums[6] = 1이 되므로 counter[1] = 3이 된다. 곧 i가 6이 될 때 가장 큰 횟수가 되므로 루프가 끝나기 전에 처리할 수 있게 된다.
    while stack and counter[nums[stack[-1]]] < counter[nums[i]]:
        # stack.pop()을 하는 이유 1. while문 첫번 째로 되돌아 갔을 때 조건의 값이 바뀐게 없기 떄문에 무한루프에 빠진다. 2. pop한 리스트 자리에 값을 대입하기 위해.
        ngf[stack.pop()] = nums[i]
    stack.append(i)

print(*ngf)
