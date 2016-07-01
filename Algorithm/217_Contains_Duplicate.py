class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for x in nums:
            if x in d:
                return True
            else:
                d[x] = 1
        return False
