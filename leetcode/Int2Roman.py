class Solution:
    def roman(self, num:int, one:str, five:str, ten:str) -> str:
        if num==9: return one+ten
        if num==4: return one+five
        
        ret = ''
        if num>=5:ret+=five
        for _ in range(num%5):
            ret+=one
        return ret
    
    def intToRoman(self, num: int) -> str:
        num_list = list(str(num))
        num_list = list(map(lambda x : int(x),num_list))
        if len(num_list) != 4:
            for _ in range(4-len(num_list)):
                num_list.insert(0,0)
        print(num_list)
        answer = self.roman(num_list[0], 'M', 'A', 'A') + self.roman(num_list[1], 'C', 'D', 'M') + self.roman(num_list[2], 'X', 'L', 'C') + self.roman(num_list[3], 'I', 'V', 'X')
        return answer

f = Solution()
print(f.intToRoman(3989))




