class Solution(object):
    def maxProduct(self, n):

        dgt1 = 0
        dgt2 = 0

        while n > 0:
            rem = n % 10

            if rem > dgt1:
                dgt2 = dgt1
                dgt1 = rem

            elif rem > dgt2:
                dgt2 = rem

            n //= 10

        return dgt1 * dgt2



        

"""
str_n = str(n)
max_pdt = 0
l = 0
r = l+1
while r < len(str_n):
    pdt = int(str_n[l]) * int(str_n[r])
    max_pdt = max(max_pdt, pdt)
    l += 1
    r += 1

return pdt"""

"""for i in range(len(str_n)-1):
    pdt = int(str_n[i]) *  int(str_n[i+1])
    max_pdt = max(max_pdt, pdt)"""


        