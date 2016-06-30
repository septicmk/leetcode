class Solution(object):
    def isAnagram(self, s, t):
        _ = [0]*26
        def func(v,t):
            _[ord(v)-ord('a')]+=t
        map(lambda x : func(x,1), s)
        map(lambda x : func(x,-1), t)
        return True if len(filter(lambda x : x !=0, _))==0  else False

