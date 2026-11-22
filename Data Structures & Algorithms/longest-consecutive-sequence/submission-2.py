class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert nums into a hash set
        # For each num, if num - 1 does not exist, this num is a start of a seq
        # If num is start of a seq, then...
            # In a while loop with incrementer i, keep adding to a streak if num + i exists in set
            # Replace maxStreak when streak exceeds it
        
        # Boundary method (one pass)
            # Runtime: O(n)
            # Space: O(n) -- to store a hash map

            # Each number will be mapped to the length of its current sequence

            # As we iterate through the array, the length of the seq containing a number
            # is simply 1 (itself) + the length of the sequence containing a number before it
            # and the length of the sequence containing the number after it

            # If the length of a sequence becomes more than 1, make sure to update any sequences
            # that also contain the number we just added

            # Repeating nums can simply be skipped

            # Along the way, store the max length of a sequence and finally return it.

        max_length = 0
        hm = {}

        for i in range(len(nums)):
            n = nums[i]

            if not hm.get(n):
                hm[n] = 1 + hm.setdefault(n-1, 0) + hm.setdefault(n+1, 0)

                k = n - 1
                while hm.get(k):
                    hm[k] = hm[n]
                    k -= 1

                k = n + 1
                while hm.get(k):
                    hm[k] = hm[n]
                    k += 1

                if hm[n] > max_length:
                    max_length = hm[n]
        
        return max_length



                



