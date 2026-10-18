class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Set common prefix to first word
        # For each word:
        # Compare prefix to next word by iterating through characters
        # When characters differ, change prefix to the substring of matching characters
        # Runtime: O(n) Space: O(1)
        strs = sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]
