class Solution(object):
    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, '#':0}
        tot,last = 0,0
        s += '#'
        for x in s:
            tmp = d[x]
            if last < tmp:
                tot -= last
            else :
                tot += last
            last = tmp
        return tot



