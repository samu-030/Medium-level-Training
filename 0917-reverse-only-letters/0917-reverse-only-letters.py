class Solution(object):
    def reverseOnlyLetters(self, s):
        s = list(s)
        l = 0
        r = len(s)-1

        while l < r:
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

            if not s[l].isalpha():   
                l += 1

            if not s[r].isalpha():
                r -= 1

        return "".join(s)    