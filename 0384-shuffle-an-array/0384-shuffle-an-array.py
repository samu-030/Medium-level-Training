class Solution(object):

    def __init__(self, nums):
        from copy import deepcopy

        self.orgnl = deepcopy(nums)
        self.curr = deepcopy(nums)

    def reset(self):
        self.curr = self.orgnl[:]
        return self.curr
        
    def shuffle(self):
        from random import shuffle
        shuffle(self.curr)
        return self.curr    


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()