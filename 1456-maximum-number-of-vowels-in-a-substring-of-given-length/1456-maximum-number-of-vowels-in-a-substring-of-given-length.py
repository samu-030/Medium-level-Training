class Solution(object):
    def maxVowels(self, s, k):
        
        res = 0
        current = 0
        vowels = "aeiou"

        for i, v in enumerate(s):

            if i >= k:
                if s[i-k] in vowels:
                    current -= 1

            if s[i] in vowels:
                current += 1
        
            res = max(current, res)

        return res


        