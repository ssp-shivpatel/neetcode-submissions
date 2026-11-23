class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix Sum
        # Runtime: O(n)
        # Space: O(n)
        
        # Iterate through the array
            # Track the curr sum accrued to get to an element (inclusive)
            # At each element, a valid sum subarray exists for each prefix of nums
            # you can remove from the current subarray (subarr from the first element
            # to the current element) that leaves remaining elements summing to k
            # We can store prefixes by mapping their sums to counts in a hash table
                # Initalize empty prefix with sum = 0, which represents when
                # a valid sum subarray is the curr subarray
            # Therefore, for each element, if the hash map contains a sum equal to
            # diff = curr_sum - k, we can increment count of subarrays by count of 
            # prefixes that sum to diff (i.e. prefix_counts[diff])

            prefix_counts = defaultdict(int)
            prefix_counts[0] = 1 
            curr_sum = 0
            res = 0

            for i in range(len(nums)):
                curr_sum += nums[i]
                diff = curr_sum - k
                
                res += prefix_counts[diff]
                prefix_counts[curr_sum] += 1 
            
            return res


        # Old Solutions:

        # Brute Force
        # O(n^2) runtime
        # O(1) space
        # Iterate through array n times, with each number as a start of a new set of 
        # of subarrays
        # For each iteration, iterate through remaining elements of array,
        # adding to count of subarrays whenever current sum of elements = k

        # subarr_count = 0
        # for i in range(len(nums)):
        #     curr_sum = 0

        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]

        #         if curr_sum == k:
        #             subarr_count += 1
        
        # return subarr_count

        # One Pass Hash Map
        # O(n^2) runtime
        # O(n) space
        # Iterate through the array once
            # Add current element as new entry to hash map
            # Add current element to each pre-existing entry
                # If this entry's value is k, increment count of subarrays
        

        
        
       
            