from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):

        if len(word1)  != len(word2):
            return False

        c1 = Counter(word1)
        c2 = Counter(word2)

        if set(c1.keys()) != set(c2.keys()):
            return False

        return True if sorted(c1.values()) == sorted(c2.values()) else False

        """if len(word1) != len(word2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in word1:
            freq1[ord(i) - ord('a')] += 1

        for i in word2:
            freq2[ord(i) - ord('a')] += 1

        for i in range(26):
            if (freq1[i] == 0 and freq2[i] > 0) or (freq1[i] > 0 and freq2[i] == 0):
                return False

        freq1.sort()
        freq2.sort()

        return True if freq1 == freq2 else False
        """