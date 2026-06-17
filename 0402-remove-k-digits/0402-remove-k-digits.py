class Solution(object):
    def removeKdigits(self, num, k):
        
        res = []

        for i in num:

            while (k and res and res[-1] > i):
                res.pop()
                k -= 1

            res.append(i)

        while (k > 0):
            res.pop()
            k -= 1

        result = "".join(res).lstrip('0')

        return result if result else "0"
        