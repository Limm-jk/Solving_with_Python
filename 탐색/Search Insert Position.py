class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        while len(nums) != index:
            if nums[index] >= target:
                break
            index += 1
        return index