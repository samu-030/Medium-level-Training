class Solution(object):
    def findMatrix(self, nums):
        matrix = []
        
        for num in nums:
            placed = False
            
            for row in matrix:
                if num not in row:
                    row.append(num)
                    placed = True
                    break
                    
            if not placed:
                matrix.append([num])
                
        return matrix


"""row1 = []
row2 = []
row3 = []
seen1 = set()
seen2 = set()

for i in nums:
    if i not in seen1:
        seen1.add(i)
        row1.append(i)
    elif (i in seen1) and (i not in seen2):
        seen2.add(i)
        row2.append(i)
    else:
        row3.append(i)

if not row3:
    matrix = [row1, row2]
elif not row2:
    matrix = [row1]
else:
    matrix = [row1, row2, row3]

return matrix"""