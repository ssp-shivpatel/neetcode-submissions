class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:        
        unique = len(nums)
        i = 0
        j = len(nums) - 1
        while(i <= j):
            if(nums[i] == val):
                nums[i] = nums[j]
                j -= 1
                unique -= 1
            else:
                i += 1

        return unique
        