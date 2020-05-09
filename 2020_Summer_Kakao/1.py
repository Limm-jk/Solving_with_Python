def isRight(hand):
    ans = True
    if hand == "left":
        ans = False
    return ans

def Num2Loc(num):
    ans = []
    if num == 0:
        ans = [1,3]
    else:
        an1 = (num+2)%3
        an2 = int((num+2)/3)-1
        ans = [an1,an2]
    return ans

def solution(numbers, hand):
    arr = list(numbers)#입력을 배열로 저장
    ans_arr = [] #답을 누적
    
    r_loc = [2,3]
    l_loc = [0,3]
    
    for i in range(len(arr)):
        if arr[i]%3 == 1:
            ans_arr.append('L')
            l_loc = Num2Loc(arr[i])
        elif (arr[i]%3 == 0) and (arr[i] != 0):
            ans_arr.append('R')
            r_loc = Num2Loc(arr[i])
        else:
            curLoc = Num2Loc(arr[i])
            L_dif = abs(curLoc[0]-l_loc[0])+abs(curLoc[1]-l_loc[1])
            R_dif = abs(curLoc[0]-r_loc[0])+abs(curLoc[1]-r_loc[1])
            if L_dif > R_dif:
                ans_arr.append('R')
                r_loc = curLoc
            elif L_dif < R_dif:
                ans_arr.append('L')
                l_loc = curLoc
            else:
                if isRight(hand):
                    ans_arr.append('R')
                    r_loc = curLoc
                else:
                    ans_arr.append('L')
                    l_loc = curLoc
    
    answer = ''.join(ans_arr)
    return answer