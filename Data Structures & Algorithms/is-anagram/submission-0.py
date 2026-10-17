class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a dictionary that stores letters as keys,
        # frequencies as values
        sDict = {}
        tDict = {}

        # Iterate through the chars of the first word, add letters and frequencies
        # to dictionary
        for letter in s:
            if sDict.get(letter):
                sDict[letter] += 1
            else:
                sDict[letter] = 1

        # Iterate through second word, add letters and freqs to second dictionary
        for letter in t:
            if tDict.get(letter):
                tDict[letter] += 1
            else:
                tDict[letter] = 1


        # Make sure key/value pair in both dictionaries are  the same
        if len(sDict) != len(tDict):
            return False


        for let in sDict.keys():
            if sDict[let] != tDict.get(let):
                return False
        
        return True
        