# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        
        LL_arr = []
        temp = head
        res = []

        while temp != None:
            LL_arr.append(temp.val)
            temp = temp.next

        left = 0
        right = len(LL_arr)-1

        while(left < right):
            sum_ = LL_arr[left] + LL_arr[right]
            res.append(sum_)

            left+=1
            right-=1

        return max(res)

        