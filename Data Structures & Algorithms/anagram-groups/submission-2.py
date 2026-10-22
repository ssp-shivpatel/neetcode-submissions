from collections import defaultdict

class Solution:
        # Sort each word's letters into alphabetical order in a separate list, 
        # ordered_words
        # Map an alphabetically ordered word with a list of its anagrams in a dict
        # Return a list representation of the dict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for i in range(len(strs)):
            sortedS = ''.join(sorted(strs[i]))
            anagrams[sortedS].append(strs[i])
            
        return list(anagrams.values())


        

