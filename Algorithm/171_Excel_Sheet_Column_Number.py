class Solution(object):
    def titleToNumber(self, s):
        ret, p = 0, 1
        for i in range(len(s)):
            tmp = ord(s[len(s)-i-1])-ord('A') + 1
            ret += tmp*p
            p *= 26
        return ret
            

