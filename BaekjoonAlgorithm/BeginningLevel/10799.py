# ironbar = list(input())

# laser = 0
# count = 0
# iron = 0
# for i in ironbar:
#     # 레이저 찾기
#     if i == "(":
#         count += 1
#     if i == ")":
#         if count == 1:  #레이저면(수정필요)
#             laser += 1
#             count = 0
#         # 쇠막대기 안에 레이저가 몇개 들어가있나
#         elif count > 1:
#             iron += laser + 1
#             count = 0

ironbar = list(input())
laser = 0
count_l = 0
count_r = 0
iron = 0
isR = 0

for i in range(len(ironbar)):
        if i+1 < len(ironbar):
            if ironbar[i+1] != ")" and ironbar[i] == "(":
                count_l += 1
            elif ironbar[i] == "(" and ironbar[i+1] == ")":

                if count_l != 0:
                    laser += 1
                isR = 1
                
            elif isR == 0 and ironbar[i] == ")":
                count_r += 1

            else:
                isR = 0

            if count_l == count_r:
                iron = iron + (count_l * laser)
                print("i", i)
                print("count_l",count_l,"count_r",count_r,"laser",laser)
                count_l = 0
                count_r = 0
        else:
            continue
        
print(iron)
