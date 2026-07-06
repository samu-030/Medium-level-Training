import heapq
 
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        
        if not nums1 or not nums2 or k == 0:
            return []
        
        min_heap = []
        res = []
        
        for i in range(min(len(nums1), k)):
            pair_sum = nums1[i] + nums2[0]
            heapq.heappush(min_heap, (pair_sum, i, 0))
            
        while min_heap and len(res) < k:
            current_sum, i, j = heapq.heappop(min_heap)
            
            res.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2):
                next_sum = nums1[i] + nums2[j + 1]
                heapq.heappush(min_heap, (next_sum, i, j + 1))
                
        return res



"""sum_ = 0
res = []

for i in range(len(nums1)):
    for j in range(len(nums2)):
        sum_ = nums1[i] + nums2[j]
        res.append((sum_, [nums1[i], nums2[j]]))

res.sort()

pairs = []
for pair_sum, pair in res[:k]:
    pairs.append(pair)


return pairs"""