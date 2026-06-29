class Solution(object):
    def findClosestElements(self, arr, k, x):

        def custom_sorting_rule(num):
            distance = abs(num - x)
            return (distance, num)
        
        sorted_by_distance = sorted(arr, key=custom_sorting_rule)
        
        closest_k_elements = sorted_by_distance[:k]
        
        final_sorted_result = sorted(closest_k_elements)
        
        return final_sorted_result


"""arr.sort()
n = len(arr)

if n/x <= x:
    return arr[:k]
else:
    return arr[k:]"""
        