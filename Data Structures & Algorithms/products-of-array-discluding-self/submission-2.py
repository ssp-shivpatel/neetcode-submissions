class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force Method
            # Runtime: O(n^2) Space: O(2n)
            # Iterate through entire array twice
            # Multiply every number in array, ignoring num[i], and append to output
        
        # Division Method 
            # Runtime: O(2n) Space: O(2n)
            # Iterate through entire away once to find total product, ignoring a singular zero term.
            # Iterate through array again, appending (total product / nums[i]) to output
            # Edge cases:
                # If there's one zero in the array, we know all products are zero except at zero's index
                # When building output at this index, just append total_product
                # If there's >=2 zeros in the array, return all zero output
               
            # total_product = 1
            # zeroFound = False
            # output = []

            # for i in range(len(nums)):
            #     if(nums[i] == 0):
            #         if zeroFound:
            #             return [0] * len(nums)
            #         zeroFound = True
            #     else:
            #         total_product *= nums[i]
            
            # for i in range(len(nums)):
            #     if(nums[i] == 0):
            #         output.append(total_product)
            #     elif zeroFound:
            #         output.append(0)
            #     else:
            #         output.append(total_product // nums[i])
            
            # return output

        # Prefix/Suffix Method
            # Runtime: O(2n) Space: O(4n)
                # Iterate through entire array from left to right to build a prefix product array
                    # Each index contains the product of only indices before it (1 if first elem)
                # Iterate through entire array from right to left to build a suffix product array
                    # Each index contains the product of only the indices after it (1 if last elem)
                # Build output array (make the same size as nums)
                    # Each index contains its own prefix product times its suffix product

        # prefix_products = [0] * len(nums)
        # prefix_products[0] = 1

        # for i in range(1, len(nums)):
        #     prefix_products[i] = nums[i - 1] * prefix_products[i - 1]
        
        # suffix_products = [0] * len(nums)
        # suffix_products[len(nums) - 1] = 1

        # for i in range(len(nums) - 2, -1, -1):
        #     suffix_products[i] = nums[i + 1] * suffix_products[i + 1]

        # output = []
        # for i in range(len(nums)):
        #     output.append(prefix_products[i] * suffix_products[i])
        
        # return output

        # Optimal Prefix/Suffix Method
        # Runtime: O(n) Space: O(2n)
        # Use output array to store prefix products
        # Then, use the same array as final output by multiplying each element to its original    
        # value to the right from right to left, which essentially multiplies each element by its 
        # suffix product

        output = []
        output.append(1)

        for i in range(1, len(nums)):
            output.append(nums[i - 1] * output[i - 1])
        
        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i + 1]
            output[i] *= postfix
        
        return output
        

            


