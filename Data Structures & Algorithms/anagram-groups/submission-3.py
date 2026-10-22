from collections import defaultdict

class Solution:
        # Sort each word's letters into alphabetical order in a separate list, 
        # ordered_words
        # Map an alphabetically ordered word with a list of its anagrams in a dict
        # Return a list representation of the dict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in range(len(strs)):
            freqs = [0] * 26
            for char in strs[i]:
                freqs[ord(char) - 97] += 1
            
            freqTuple = tuple(freqs)
            anagrams.setdefault(freqTuple, [])
            anagrams[freqTuple].append(strs[i])
        
        return list(anagrams.values())


        

