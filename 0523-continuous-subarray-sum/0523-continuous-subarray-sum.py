class Solution(object):
    def checkSubarraySum(self, nums, k):
        
        rem_map = {0 : -1}
        sum = 0

        for i, num in enumerate(nums):

            sum += num
            rem = sum % k

            if rem in rem_map:

                if i - rem_map[rem] >= 2:
                    return True
            else:
                rem_map[rem] = i

        return False