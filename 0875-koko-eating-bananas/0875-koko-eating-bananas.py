class Solution(object):
    def minEatingSpeed(self, piles, h):
        
        low = 1
        high = max(piles)

        res = high

        while low <= high:

            mid = (low + high)//2

            ttl_hrs = 0
            for i in piles:
                ttl_hrs += (i + mid-1) // mid

            if ttl_hrs <= h:
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res

        
        