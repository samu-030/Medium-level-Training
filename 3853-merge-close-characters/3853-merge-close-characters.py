class Solution(object):
    def mergeCharacters(self, s, k):

        chars = list(s)

        while True:

            changed = False
            n = len(chars)


            for i in range(n):
                for j in range(i+1, min(i+k+1, n)):

                    if chars[i] == chars[j]:

                        chars.pop(j)
                        changed = True
                        break

                if changed:
                    break

            if not changed:
                break

        return "".join(chars)
        

        
        """loop through s:
           if i == j:
               if i - j <= k:
                  merge i and j

        return s"""
           
        