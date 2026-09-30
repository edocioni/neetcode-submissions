class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        i = 0
        while i <= len(nums):
            if i not in nums_set:
                return i
            i += 1
        return i