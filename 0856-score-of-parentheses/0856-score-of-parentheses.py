class Solution(object):
    def scoreOfParentheses(self, s):

        score = 0
        depth = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == '(':
                    score += 1 << depth
                    
        return score

        
"""cnt = 0
stack = []

for i in s:
    if i == "(":
        cnt += 1

return cnt"""
        