class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsFrequencies = {}
        for num in nums:
            if numsFrequencies.get(num):
                return True
            else:
                numsFrequencies[num] = 1
        return False
        