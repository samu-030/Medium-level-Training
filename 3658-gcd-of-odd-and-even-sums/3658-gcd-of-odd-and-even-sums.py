class Solution(object):
    def gcdOfOddEvenSums(self, n):

        odd = n * n
        even = n * (n + 1)

        while even:
            odd, even = even, odd % even

        return odd

        


        