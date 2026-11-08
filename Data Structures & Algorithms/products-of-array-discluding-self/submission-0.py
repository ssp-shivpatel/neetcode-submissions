class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force Method
            # Runtime: O(n^2) Space: O(2n)
            # Iterate through entire array twice
            # Multiply every number in array, ignoring num[i], and append to output
        
        # Division Method (DOESN'T WORK unless you count zeros and do an extra iteration for edge case)
            # Doesn't work due to cases of single zero, where the product that ignores the zero
            # should be non-zero
            # Runtime: O(2n) Space: O(2n)
            # Iterate through entire away once to find total product
            # Iterate through array again, appending (total product / nums[i]) to output
            # If nums[i] = 0, just append total_product


        # Prefix/Suffix Method
            # Runtime: O(2n) Space: O(4n)
                # Iterate through entire array from left to right to build a prefix product array
                    # Each index contains the product of only indices before it (1 if first elem)
                # Iterate through entire array from right to left to build a suffix product array
                    # Each index contains the product of only the indices after it (1 if last elem)
                # Build output array (make the same size as nums)
                    # Each index contains its own prefix product times its suffix product

        prefix_products = [0] * len(nums)
        prefix_products[0] = 1

        for i in range(1, len(nums)):
            prefix_products[i] = nums[i - 1] * prefix_products[i - 1]
        
        suffix_products = [0] * len(nums)
        suffix_products[len(nums) - 1] = 1

        for i in range(len(nums) - 2, -1, -1):
            suffix_products[i] = nums[i + 1] * suffix_products[i + 1]

        output = []
        for i in range(len(nums)):
            output.append(prefix_products[i] * suffix_products[i])
        
        return output
        

            


