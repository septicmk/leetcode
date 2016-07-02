class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        elif num < 7:
            return True
        else:
            while(num&1 == 0):
                num /= 2
            while(num%3 == 0):
                num /= 3
            while(num%5 == 0):
                num /=5
            if num == 1:
                return True
            else:
                return False
        
