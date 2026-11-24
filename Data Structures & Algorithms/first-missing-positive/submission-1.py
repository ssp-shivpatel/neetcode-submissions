class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Hash Map
        # Runtime: O(n)
        # Space: O(n)

        # Initalize res as 1
        # Iterate through the array
            # Add each element into a hash set
            # While res exists in the hash set, increment by 1
        res = 1
        appears = set()
        for num in nums:
            appears.add(num)
            while res in appears:
                res += 1
        return res


        # Cycle Sort
        # Runtime: O(n)
        # Space: O(1)

        # Iterate through the array
            # We know the min positive sequence of numbers must start at 1.
            # We can build up this sequence at the start of the arr:
                # Whenever we find a number, swap it with its correct index.
                    # I.e. i + 1, if it's out of bounds - do not swap.
                # Start at index 0 with 1, continue onwards.
                # Do not swap negative numbers or zero.
        # Iterate through the array once more to check for discrepancies.
            # If nums[i] != i + 1, the missing int is i + 1.
        # If we get to the end of arr without discrepancy, the entire list is
        # a min positve sequence, meaning res = len(nums) + 1.

        
        for i in range(len(nums)):
            if nums[i] > 0 and i + 1 < len(nums):
                temp = nums[nums[i] + 1]
                nums[nums[i] + 1] = nums[i]
                nums[i] = temp
        
        res = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res = i + 1
                break
        
        return res
