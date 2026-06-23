class Solution(object):
    def lengthOfLongestSubstring(self, s):

        unique = set()
        left = 0
        max_count = 0

        #i = right pointer
        for i in range(0, len(s)):

            while s[i] in unique:
                unique.remove(s[left])
                left += 1

            unique.add(s[i])

            max_count = max(max_count, i - left + 1)

        return max_count



        