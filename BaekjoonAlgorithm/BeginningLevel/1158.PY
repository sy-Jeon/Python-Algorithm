n, k = map(int, input().split())

person = list(range(1, n + 1))
dead_person = []
index = 0

for i in range(n):
    index += k - 1

    if index >= len(person):
        index %= len(person)

    dead_person.append(person.pop(index))
    
print("<", ", ".join(map(str, dead_person)), ">", sep= "")



'''
Time over
'''
# n, k = map(int, input().split())

# queue = list(range(1, n + 1))
# death_queue = []
# index = 0
# count = 1

# while n != len(death_queue):
#     if index < n:
#         index += 1
#     else:
#         index = 1
#     print(index)
#     if count != k:
#         queue.append(queue[0]) #value
#         queue.pop(0) #index
#         count += 1
#     else:
#         death_queue.append(queue[0])  #value
#         queue.pop(0) #index
        
#         if not queue:
#             break

#         count = 1
#     print("queue: ",queue)
#     print("death_queue: ",death_queue)
# print("<", ", ".join(map(str, death_queue)), ">", sep= "")