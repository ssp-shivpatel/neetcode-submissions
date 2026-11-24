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

        # Notes:
        # A new number can only combine a max of two sequences
            # This does not need to include the min sequence
