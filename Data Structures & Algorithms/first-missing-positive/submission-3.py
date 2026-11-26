class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Cycle Sort
        # Runtime: O(n)
        # Space: O(1)

        # Compose a sequence of 1, 2, 3... starting at index 0 within nums
        # The first missing number in this seq is the first missing positive
        
        # Iterate through the array
            # If the element is 0 or negative, skip
            # If we're swapping duplicates, skip
            # Swap nums[i] with nums[nums[i] - 1] (ex. swapping 1 into index 0)
                # If the swap would be out of bounds, skip
            # Continue swapping until we're forced to skip
        # Check the array for missing #'s
            # If nums[i] != i + 1, this number is skipped and the first missing #
            # is i + 1
        # If we pass through the whole arr, the arr is a full sequence with the miss
        # number being len(nums)

        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] - 1 >= len(nums):
                i += 1
                continue
            
            if nums[i] == nums[nums[i] - 1]:
                i += 1
                continue
            
            temp = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = temp

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


        
