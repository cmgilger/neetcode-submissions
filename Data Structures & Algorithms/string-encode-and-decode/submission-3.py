class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            #length, #, string
            res += str(len(s)) + "#" + s
        return res
        # example: Hello, World -> 5#Hello5#World

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # looks for # beginning at the current location in the encoded message
            j = s.find("#", i)
            # j = index of #
            # length = character ahead of # (5#Hello; i = 0, j = 1; s[i:j] = 5)
            length = int(s[i:j])
            # append everything from behind the hash to the end of length
            res.append(s[j+1:j+1+length])
            # new index at the end of the current word
            i = j + 1 + length
        return res