# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        
        LL_arr = []
        temp = head

        while temp != None:
            LL_arr.append(temp.val)
            temp = temp.next

        left = 0
        right = len(LL_arr)-1
        max_sum = 0

        while(left < right):
            sum_ = LL_arr[left] + LL_arr[right]
            if max_sum < sum_:
                max_sum = sum_
                
            left+=1
            right-=1

        return max_sum

        