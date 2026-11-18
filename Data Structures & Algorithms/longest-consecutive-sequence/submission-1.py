class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the array into a hash set to easily check what values are in the array
        numSet = set(nums)
        
        # Build sequences only for starting nums (nums where its previous # is not in arr)
        # Keep track of the length of the current sequence and the max length of a sequence
        # Update max_length if length of curr seq is greater
        # No need to store sequences! We only care about the length of the longest one.
        max_length = 0
        
        for i in range(len(nums)):
            if not nums[i] - 1 in numSet:
                curr = nums[i]
                curr_length = 0
                while curr in numSet:
                    curr_length += 1
                    max_length = max(curr_length, max_length)
                    curr += 1


        # Return max length
        return max_length

    