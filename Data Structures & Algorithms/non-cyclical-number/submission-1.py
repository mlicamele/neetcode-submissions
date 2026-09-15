class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumSquareDigits(num):
            s = 0
            while num != 0:
                s += (num % 10) ** 2
                num = num//10
            return s
        
        t = n
        seen = []
        while t not in seen:
            if t == 1:
                return True
            seen.append(t)
            t = sumSquareDigits(t)
            print(t)
            print(seen)
        return False