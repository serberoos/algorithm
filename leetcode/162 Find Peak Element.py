class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        pivot = (left + right)/2
        if nums.size() <= 1:
					return 0

        while(left < right):
            if nums[pivot] < nums[pivot + 1]:
                left = pivot + 1
                pivot = (left + right)/2
            else:
                right = pivot # because pivot can be a peak
                pivot = (left + right)/2
        
        return pivot