class Solution(object):
    def prefixConnected(self, words, k):

        pref_cnt = {}

        for word in words:

            if len(word) < k:
                continue

            prefix = word[:k]

            if prefix in pref_cnt:
                pref_cnt[prefix] += 1
            else:
                pref_cnt[prefix] = 1
            
        count = 0

        for value in pref_cnt.values():
            if value >= 2:
                count += 1
            

        return count
