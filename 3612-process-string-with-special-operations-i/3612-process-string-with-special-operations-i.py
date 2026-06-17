class Solution(object):
    def processStr(self, s):
        
        result = []

        for i in s:

            if i >= 'a' and i <= 'z':
                result.append(i)

            if i == "*":
                if result:
                    result.pop()

            if i == "#":
                result.extend(result)

            if i == "%":
                result = result[::-1]

        return "".join(result)