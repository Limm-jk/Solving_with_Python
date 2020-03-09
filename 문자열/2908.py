#세자리 숫자 숫자 뒤집어서 크기비교
inputList = list(input())
for i in range(len(inputList)):
    if i != 3:
        inputList[i] = int(inputList[i])
Num1 = 100*inputList[2]+10*inputList[1]+inputList[0]
Num2 = 100*inputList[6]+10*inputList[5]+inputList[4]

result = Num1 if Num1 > Num2 else Num2
print(result)
# if result:
#     print(Num1)
# else:
#     print(Num2)