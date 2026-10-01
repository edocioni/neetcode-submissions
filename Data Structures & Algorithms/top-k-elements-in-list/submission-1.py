class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostfrequent=[]
        frequencies={}
        i=0
        while i<len(nums):
            frequencies[nums[i]]=frequencies.get(nums[i],0)+1
            i+=1
        i=0
        frequencies.items()
        sorted_frequencies=sorted(frequencies.items(), key=lambda couple: couple[1], reverse=True)
        while i<k:
            mostfrequent.append(sorted_frequencies[i][0])
            i+=1
        return mostfrequent
