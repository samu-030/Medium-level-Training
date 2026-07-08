class Solution(object):
    def reverse(self, x):

        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        res = rev * sign

        if res < -2**31 or res > 2**31-1:
            return 0

        return res
        
"""x_rev = str(abs(x))[::-1]

res = int(x_rev) if x >= 0 else -int(x_rev)

if res < -2**31 or res > 2**31-1:
    return 0

return res"""


        