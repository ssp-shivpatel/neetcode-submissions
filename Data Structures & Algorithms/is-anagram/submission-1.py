class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Create dictionaries that stores letters as keys,
        # frequencies as values
        sDict, tDict = {}, {}

        # Iterate through the chars of each word, add letters and frequencies
        # to dictionaries
        for i in range(len(s)):
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
            tDict[t[i]] = 1 + tDict.get(t[i], 0)


        # Make sure key/value pair in both dictionaries are  the same
        return sDict == tDict
        