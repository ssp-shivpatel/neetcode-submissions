class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            j = indices.get(target - num)
            if j != None:
                return [j, i]
            else:
                indices[num] = i
        