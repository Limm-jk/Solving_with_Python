# # 97 ~ 122
# # 65 ~ 90

# for i in range(1,10):
#     print("'",i,"',", end="", sep = "")

# for i in range(65,91):
#     print("'",chr(i),"',", end="", sep = "")

# for i in range(97,123):
#     print("'",chr(i),"',", end="", sep = "")
# 
status = 0
oldStatus = -1

while(True):
    status = input()
    if(status != oldStatus): 
        print(status)
    oldStatus = status


