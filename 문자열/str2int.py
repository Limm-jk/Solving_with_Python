import sys

class Solution:
    def myAtoi(self, s: str) -> int:
        sL = list(s)
        ans_list = []
        flag = 0
        
        while True:
            if len(sL) == 0:
                break
            
            if sL[0] == ' ':
                sL.pop(0)
                if flag == 1:
                    break
                continue
            
            if sL[0].isdigit() or sL[0] == '+' or sL[0] == '-':
                if sL[0] == '+' or sL[0] == '-':
                    if flag == 2:
                        ans_list =[]
                        break
                    if flag == 1:
                        break
                    flag = 2
                        
                ans_list.append(sL.pop(0))
                if flag == 0: flag = 1
            else:
                break
                
        ans = ''.join(ans_list)
        if len(ans_list) == 0:
            ans = 0
        # print(ans)
       

        ans = int(ans)
        if ans > pow(2, 31) - 1: 
            ans = pow(2, 31) -1 
        elif ans < pow(2, 31) * (-1): 
            ans = pow(2, 31) * (-1)
        
        return int(ans)
        
f = Solution()
print(f.myAtoi("   +-42"))