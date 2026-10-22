from collections import defaultdict

class Solution:
        # Sort each word's letters into alphabetical order in a separate list, 
        # ordered_words
        # Map an alphabetically ordered word with a list of its anagrams in a dict
        # Return a list representation of the dict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordered_words = [""] * len(strs)
        anagrams = defaultdict(list)

        for i in range(len(strs)):
            ordered_words[i] = ''.join(sorted(strs[i]))
            anagrams[ordered_words[i]].append(strs[i])
            
        return list(anagrams.values())


        

