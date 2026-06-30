class Solution(object):
    def maxChunksToSorted(self, arr):

        curr_sum, expected_sum, chunks = 0, 0, 0

        for i in range(len(arr)):
            curr_sum += arr[i]
            expected_sum += i

            if curr_sum == expected_sum:
                chunks += 1
                
        return chunks
        