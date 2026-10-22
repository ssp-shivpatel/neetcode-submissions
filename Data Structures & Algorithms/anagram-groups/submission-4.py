from collections import defaultdict

class Solution:
        # Create a hash table with letter frequency arrays as keys and arrays with 
        # the actual strings as values. This is because strings w/ same letter freqs 
        # = anagrams.
        # Convert arrays to tuples since hash table keys must be immutable.
        # Simply return the hash table's values as a list (List[List[str]]).

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


        

