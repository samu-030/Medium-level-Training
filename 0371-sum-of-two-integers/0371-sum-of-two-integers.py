class Solution(object):
    def getSum(self, a, b):
        #return a ^ b

        bit_xor = a ^ b
        and_Lshift = (a&b)<<1

        return bit_xor + and_Lshift


        