class Solution(object):
    def removeStars(self, s):

        res = []

        for i in s:
            if i == "*":
                if res:
                    res.pop()

            else:
                res.append(i)

        return "".join(res)
        

#Does not work, just tried:
"""res = ""
i = 0

while i < len(s)-1:
    if (s[i] != "*" and s[i+1]!= "*"):
        res += s[i]
        i += 1
    else:
        i+= 2
        if i < len(s)-1 and s[i] == "*":
            res = res[:-1]

        if i < len(s)-1:
            res += s[i]

return res"""

        