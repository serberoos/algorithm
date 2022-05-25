class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        indexOne = m - 1
        indexTwo = n - 1
        index = len(nums1) - 1
        
        if indexTwo < 0:
            return None
        
        while indexOne >= 0 and indexTwo >= 0:
            if nums1[indexOne] >= nums2[indexTwo]:
                nums1[index] = nums1[indexOne]
                index = index - 1
                indexOne = indexOne - 1 
            else:
                nums1[index] = nums2[indexTwo]
                index = index - 1
                indexTwo = indexTwo - 1
        # memory copy
        while indexTwo >= 0:
            nums1[index] = nums2[indexTwo]
            index = index -1
            indexTwo = indexTwo - 1