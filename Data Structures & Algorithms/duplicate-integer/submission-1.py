class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsFrequencies = set()
        for num in nums:
            if num in numsFrequencies:
                return True
            else:
                numsFrequencies.add(num)
        return False
        