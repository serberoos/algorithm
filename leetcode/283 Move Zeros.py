class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insertIndex = 0
        numIndex = 0
        
        while numIndex != len(nums):
            if nums[numIndex] != 0:
                nums[insertIndex] = nums[numIndex]
                insertIndex = insertIndex + 1
            numIndex = numIndex + 1
                
        while insertIndex != len(nums):
            nums[insertIndex] = 0
            insertIndex = insertIndex + 1