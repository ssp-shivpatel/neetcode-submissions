class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # Boyer-Moore Voting Algo (Hash Map)
            # Create a hash map that can store at most 2 candidates, since only 2 elements can potentially
            # appear in an array more than n // 3 times
            # Iterate through the array
                # Increment the current element's score
                # If there are less than 2 candidates in the hash map, we can keep that element as a candidate
                # Otherwise, if there are now >2 candidates, we must remove any element with a score of 0
                # after decreasing all candidates' score by 1 (will always be one candidate, therefore we
                # return to 2 candidates)
            # Finally, verify that the remaining candidates' count is actually > flr(n/3) and return these

        candidates = defaultdict(int)

        for num in nums:
            candidates[num] += 1

            if len(candidates) <= 2:
                continue
            
            new_candidates = defaultdict(int)

            for num, score in candidates.items():
                if score > 1:
                    new_candidates[num] = score - 1
            candidates = new_candidates
        
        res = []

        for num in candidates:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        
        return res
                

        
    