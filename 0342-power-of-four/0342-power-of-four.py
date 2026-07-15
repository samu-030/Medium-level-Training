class Solution(object):
    def isPowerOfFour(self, n):
        return n > 0 and log(n, 4).is_integer()


"""if n == 1 or (n % 4 == 0) and n > 0:
return True
return False"""
        