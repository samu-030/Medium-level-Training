class Solution(object):
    def divisibilityArray(self, word, m):

        res = []
        rem = 0
    
        for i in word:
            rem = (rem * 10 + int(i)) % m

            if rem == 0:
                res.append(1)
            else:
                res.append(0)

        return res

#Method 1 : Time limit will Exceed
#Because, on taking every sliced digits from a particularly 
#large number (i.e: 10^5), it takes more time.      
"""n = len(word)
res = []

for i in range(1,n+1):
    if int(word[:i]) % m == 0:
        res.append(1)

    else:
        res.append(0)

return res"""
