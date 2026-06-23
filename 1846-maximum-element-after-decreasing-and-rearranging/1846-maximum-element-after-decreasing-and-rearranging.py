class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        
        arr.sort()
        arr[0] = 1

        for i in range(len(arr)-1):

            if arr[i+1] - arr[i] > 1:
                arr[i+1] = arr[i] + 1

        return arr[-1]
        