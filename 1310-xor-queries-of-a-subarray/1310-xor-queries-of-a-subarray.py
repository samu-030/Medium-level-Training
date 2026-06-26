class Solution(object):
    def xorQueries(self, arr, queries):
#Method - 2 : Using a Prefix - XOR Array

        pref_arr = [0] * (len(arr)+1)

        for i in range(len(arr)):
            pref_arr[i+1] = pref_arr[i] ^ arr[i]

        res = []

        for l, r in queries:

            xor = pref_arr[r+1] ^ pref_arr[l]
            res.append(xor)

        return res

        


#Method - 1 : used nested for-loop for interating over the given two arrays
"""res = []

for query in queries:
    left = query[0]
    right = query[1]

    curr_xor = 0

    for i in range(left, right+1):
        curr_xor ^= arr[i]

    res.append(curr_xor)

return res           
"""