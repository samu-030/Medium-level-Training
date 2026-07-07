class Solution(object):
    def sumAndMultiply(self, n):
        
        x = ""
        str_n = str(n)

        for i in str_n:
            if int(i) != 0:
                x += i

        x_sum = 0
        for i in x:
            x_sum += int(i)

        try:
            return int(x) * x_sum
        except ValueError:
            return 0

        