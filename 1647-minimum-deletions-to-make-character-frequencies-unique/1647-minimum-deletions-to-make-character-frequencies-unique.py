from collections import Counter

class Solution(object):
    def minDeletions(self, s):

        count = Counter(s)
        del_count = 0

        unique = set()

        for char, freq in count.items():

            while freq > 0 and freq in unique:
                freq -= 1
                del_count += 1

            unique.add(freq)

        return del_count
        
        """freq = [0] * 26

        for i in s:
            if i not in freq:
                freq[ord("i") - ord("a")] += 1

        freq.sort()

        count = 0
        unique = set()





        for i in freq:

            count = 0
            if freq[i] == freq[i+1]:
                count += 1
            else:
                return 0
        
        return count""" 