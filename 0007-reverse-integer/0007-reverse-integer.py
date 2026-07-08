class Solution(object):
    def reverse(self, x):
        
        x_rev = str(abs(x))[::-1]

        res = int(x_rev) if x >= 0 else -int(x_rev)

        if res < -2**31 or res > 2**31-1:
            return 0

        return res


        