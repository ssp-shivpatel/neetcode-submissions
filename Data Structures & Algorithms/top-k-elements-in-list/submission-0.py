class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Runtime: O(n log n) Memory: O(n)
        # Use a dict to store frequencies of each integer
        # Iterate through nums to add frequencies for each character,
        # Sort dict keys in descending order by freqs
        # Return the first k integer keys
        # Return the output

        freqs = {}

        for i in range(len(nums)):
            freqs[nums[i]] = freqs.setdefault(nums[i], 0) + 1
        
        sorted_freqs = list(sorted(freqs.items(), key=lambda item: item[1], reverse=True))
        output = []
        for key in range(k):
            output.append(sorted_freqs[key][0])

        return output
