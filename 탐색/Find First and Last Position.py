class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = 0
        start = -1
        num = 0
        while index != len(nums):
            if nums[index] == target:
                if start == -1:
                    start = index
                else:
                    num += 1
                        
            index += 1
        if start == -1:
            return [-1,-1]
        return [start, start+num]