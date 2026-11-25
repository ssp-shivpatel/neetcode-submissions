class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix Sum
        # Runtime: O(n)
        # Space: O(n)
        
        # Use a hash table that maps prefix sums to counts of same prefix sums
        # Iterate through the array
            # Curr element represents the end of the curr sequence
            # Consider what vaid subarrays we can form by chopping off prefixes
            # of curr sequence
                # This includes chopping off no prefix!
            # If sum of remaining elements after removing prefix = k, 
            # we can increment res

            # Store the curr sum of each element in the curr sequence by
            # adding to it as we iterate
            # We want to check if k = curr_sum - prefix_sum  
            # Look for prefix_sum in hashmap: curr_sum - k
                # Increment res by counts[prefix_sum] (valid subarrays produced
                # by chopping off prefixes that sum to prefix_sum)
            # Afterwards, inc counts[curr_sum] += 1 so the next elements can use
            # the curr element as part of prefixes

            # Edge Case: Make sure to intialize counts[0] = 1 to count first element
            # being = k as a valid subarray

        counts = defaultdict(int)
        curr_sum = 0
        res = 0
        counts[0] = 1

        for i in range(len(nums)):
            curr_sum += nums[i]
            res += counts[curr_sum - k]
            counts[curr_sum] += 1

        return res
        

            
