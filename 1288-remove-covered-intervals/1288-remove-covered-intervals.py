class Solution(object):
    def removeCoveredIntervals(self, intervals):
        
        n = len(intervals)
        removed = [False] * n
        
        for i in range(n):
            for j in range(n):
                if i == j or removed[i] or removed[j]:
                    continue
                
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    removed[j] = True
                    
                elif intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                    removed[i] = True
                    
        return removed.count(False)        