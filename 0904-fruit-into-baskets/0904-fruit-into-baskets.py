class Solution(object):
    def totalFruit(self, fruits):

        basket = {}
        max_count = 0
        left = 0

        for right in range(len(fruits)):

            curr_frt = fruits[right]
            basket[curr_frt] = basket.get(curr_frt, 0) + 1

            while len(basket) > 2:

                l_frt = fruits[left]
                basket[l_frt] -= 1

                if basket[l_frt] == 0:
                    del basket[l_frt]

                left += 1

            max_count = max(max_count, right-left+1)

        return max_count

