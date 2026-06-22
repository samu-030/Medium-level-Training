class Solution(object):
    def getDescentPeriods(self, prices):
        
        ttl_prd = 1
        curr_streak = 1

        for i in range(1, len(prices)):

            if prices[i] == prices[i-1] - 1:
                curr_streak += 1
            else:
                curr_streak = 1

            ttl_prd += curr_streak

        return ttl_prd

        