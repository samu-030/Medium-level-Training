class Solution(object):
    def countCommas(self, n):

        count = 0
        threshold = [10**3, 10**6, 10**9, 10**12, 10**15]

        for t in threshold:
            if n >= t:
                count += (n - t + 1)

        return count
        