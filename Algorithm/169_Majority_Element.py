class Solution(object):
    def majorityElement(self, nums):
        cnt,cur = 0,0
        for x in nums:
            if cnt == 0:
                cnt += 1
                cur = x
            elif cur == x:
                cnt += 1
            else :
                cnt -= 1
        return cur

