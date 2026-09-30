class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        n=-1
        for num in nums:
            if num==target:
                return i
            i+=1
        return n