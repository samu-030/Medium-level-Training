class Solution(object):
    def maxIceCream(self, costs, coins):
        
        costs.sort()
        res = 0

        for i in costs:
            if i > coins:
                break

            res += 1
            coins -= i

        return res

