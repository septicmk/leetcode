class Solution(object):
    def isHappy(self, n):
        t = {}
        while(n!=1):
            if n in t:
                return False
            t[n] = 1
            n = reduce(lambda x,y: x + y, map(lambda x: int(x)**2, list(str(n))))
        return True
