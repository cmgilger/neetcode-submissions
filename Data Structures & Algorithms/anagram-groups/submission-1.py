class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create anagram dictionary
        anagram_dict = {}
        n = len(strs)

        # navigate strs
        for word in strs:
            # sort alphabetically
            sorted_key = "".join(sorted(word))
            
            if sorted_key in anagram_dict.keys():
                anagram_dict[sorted_key].append(word)

            else:
                anagram_dict[sorted_key] = [word]
        ans = []
        for grp in anagram_dict.values():
            ans.append(grp)
        return ans
