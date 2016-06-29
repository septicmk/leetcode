class Solution(object):
    def intersection(self, nums1, nums2):
        ret = []
        last = None
        j = 0
        nums1.sort()
        nums2.sort()
        for i in range(len(nums1)):
            while (j < len(nums2) and (nums1[i] > nums2[j])):
                j+=1
            if j >= len(nums2):
                break
            elif nums1[i] != last and nums1[i] == nums2[j]:
                ret.append(nums1[i])
                last = nums1[i]
                j += 1
        return ret
            

