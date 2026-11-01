class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Construct a dictionary mapping colors to their frequencies in nums.
        Replace elements starting from the beginning based on their frequencies.
        Memory: O(n); Space: O(1)
        """

        freqs = {0:0, 1:0, 2:0}
        for i in range(len(nums)):
            freqs[nums[i]] += 1
        
        index = 0
        for color, freq in freqs.items():
            while freq > 0:
                nums[index] = color
                index += 1
                freq -= 1