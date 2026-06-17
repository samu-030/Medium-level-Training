class Solution(object):
    def sumOfPrimesInRange(self, n):       

        def isPrime(num):
            if num <= 1:
                return False

            if num == 2:
                return True

            if num % 2 == 0:
                return False

            for i in range(3, int(num**0.5)+1, 2):
                if (num % i) == 0:
                    return False
            return True

        
        rev = int(str(n)[::-1])
        sum = 0

        for i in range(min(n, rev), max(n, rev)+1):
            if isPrime(i) == True:
                sum += i

        return sum
        

        '''r = int(str(n)[::-1])

        start, end = sorted([n, r])

        res = 0
        for i in range(start, end + 1):
            if i > 1 and all(i % d for d in range(2, int(i**0.5) + 1)):
                res += i

        return res'''
        