class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        
        blue = len(nums) -1
        
        while(white <= blue):
            if nums[white] == 0:
                
                nums[white], nums[red] = nums[red], nums[white]
                
                white = white + 1
                red = red + 1
                
            elif nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                
                blue = blue - 1
            else:
                white= white + 1