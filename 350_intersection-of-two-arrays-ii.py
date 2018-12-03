class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums1)<=nums2:
            for i in nums1:
                if i in nums2:
                    res.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if i in nums1:
                    res.append(i)
        return res
        
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]  
print Solution().intersect(nums1, nums2)      