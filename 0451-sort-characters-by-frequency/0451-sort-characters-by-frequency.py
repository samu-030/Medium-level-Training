class Solution(object):
    def frequencySort(self, s):

        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1

        res = ""

        while freq:
            max_char = ""
            max_cnt = 0

            for char, count in freq.items():
                if count > max_cnt:
                    max_cnt = count
                    max_char = char

            res += max_char * max_cnt

            del freq[max_char]

        return res
            
"""freq = {}

for i in s:
    freq[i] = freq.get(i,0)+1

freq_sorted = dict(sorted(freq.values()))

return "".join(freq_sorted)"""
        