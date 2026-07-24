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

            curr_seq = s[l : r+1] 

            if curr_seq in seen:
                res.add(curr_seq)
            else:
                seen.add(curr_seq)

            l += 1
            r += 1

        return list(res)
        
        