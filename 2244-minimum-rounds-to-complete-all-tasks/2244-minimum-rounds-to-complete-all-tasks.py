class Solution(object):
    def minimumRounds(self, tasks):
        
        count = Counter(tasks)
        rounds = 0

        for i in count.values():
            if i == 1:
                return -1

            rounds += (i + 2) / 3

        return rounds
        