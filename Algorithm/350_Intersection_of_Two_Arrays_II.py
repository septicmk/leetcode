class Solution(object):
    def intersect(self, nums1, nums2):
        ret = []
        nums1.sort()
        nums2.sort()
        i = 0
        for x in nums1:
            if i >= len(nums2):
                break
            while(i+1 < len(nums2) and x > nums2[i]):
                i +=1
            if x == nums2[i]:
                ret.append(x)
                i += 1
        return ret



        
