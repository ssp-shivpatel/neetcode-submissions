class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i, num in enumerate(nums):
            vals[num] = i
        
        for i, num in enumerate(nums):
            j = vals.get(target - num)
            if j and j != i:
                return [i, j]
        