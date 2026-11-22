class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Hash Map
            # Runtime: O(n)
            # Space: O(n)

            # Iterate through array, track frequencies of elements in a hash map
            # Whenever a freq updates to be > n // 3, add element to res
            # Set freq to negative value to prevent elements from being double counted in res
            # Return output

        freqs = {}
        res = []

        for num in nums:
            freqs[num] = freqs.setdefault(num, 0) + 1
            if freqs[num] > len(nums) // 3:
                res.append(num)
                freqs[num] = -len(nums) # Prevents double counting
        
        return res
        


        