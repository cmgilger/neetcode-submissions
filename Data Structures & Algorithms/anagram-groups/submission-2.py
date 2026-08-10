class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create anagram dictionary
        anagram_dict = collections.defaultdict(list)
        # navigate strs
        for word in strs:
            # sort alphabetically
            sorted_key = "".join(sorted(word))
            # append original word to anagrams
            anagram_dict[sorted_key].append(word)
        # result values list
        res = []
        # add dictionary values to list
        for value in anagram_dict.values():
            res.append(value)
        return res
