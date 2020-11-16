from typing import List

# def canJump(nums: List[int]) -> bool:
#     ans = True
#     if nums[0] == 0:
#         if len(nums) != 1:
#             ans = False
#             return ans
#     i = 1
#     while i < len(nums):
#         if nums[i] == 0:
#             n = i
#             count = 0
#             while True:
#                 if n >= len(nums) or nums[n] != 0:
#                     break
#                 n+=1
#                 count += 1
            
#             if nums[i-1] <= count:
#                 ans = False
#                 return ans
#             i = n-1
#         i += 1
#     return ans

# print(canJump([0]))

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in reversed(range(len(nums)-1)):
            if i + nums[i] >= goal:
                goal = i
            
        if goal == 0: 
            return True
        else: 
            return False
            