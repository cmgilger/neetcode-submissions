class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strip string
        s_stripped = "".join(char.lower() for char in s if char.isalnum())
        # get lengthe
        finalIndex = len(s_stripped) - 1
        # go through string
        for i in range(finalIndex):
            # compare i and (len(s)-1) - i
            if s_stripped[i] != s_stripped[finalIndex - i]:
                # if they are different, return false
                return False
            # else, continue
            elif i == finalIndex - i:
                continue
        # return true
        return True

