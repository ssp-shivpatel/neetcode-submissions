class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Set common prefix to first word
        # For each word:
        # Compare prefix to next word by iterating through characters
        # When characters differ, change prefix to the substring of matching characters
        # Runtime: O(n) Space: O(1)

        commonPrefix = strs[0]
        for i, word in enumerate(strs[1:], start=1):
            if (word == ""):
                return ""
            for j in range(len(commonPrefix)):
                if j == len(word):
                    commonPrefix = word
                    break
                if commonPrefix[j] != word[j]:
                    commonPrefix = word[:j]
                    break
        return commonPrefix
