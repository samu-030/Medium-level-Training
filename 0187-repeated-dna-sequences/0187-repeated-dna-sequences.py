class Solution(object):
    def findRepeatedDnaSequences(self, s):

        n = len(s)
        seen = set()
        res = set()

        if n < 10:
            return list(res)
            
        l = 0
        r = 9

        while(r < n):

            if s[l : r+1] in seen:
                res.add(s[l : r+1])
            else:
                seen.add(s[l : r+1])

            l += 1
            r += 1

        return list(res)
        
        