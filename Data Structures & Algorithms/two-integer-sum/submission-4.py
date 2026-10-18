class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = []
        for i in range(len(nums)):
            pairs.append([nums[i], i])
        pairs.sort()

        i = 0
        j = len(nums) - 1
        while(i < j):
            add = pairs[i][0] + pairs[j][0]
            if(add < target):
                i += 1
            elif(add > target):
                j -= 1
            else:
                return [min(pairs[i][1], pairs[j][1]),
                 max(pairs[i][1], pairs[j][1])]
        