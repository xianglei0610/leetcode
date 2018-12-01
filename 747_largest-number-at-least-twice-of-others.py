class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)<2:
            return 0
        nums_new = sorted(nums)
        if nums_new[-1]>=nums_new[-2]*2:
            return nums.index(nums_new[-1])
        else:
            return -1