class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        result = sys.maxint # 리턴할 length result
        left = 0 # left 포인터
        sum = 0  # 값 sum
        
        for index in range(0, len(nums)): #배열 index 만큼 순회
            sum = sum + nums[index] # index의 값 sum에 추가
            while sum>= target: # sum이 target 값 보다 크거나 같을 경우
                result = min(result, index + 1 - left)
                sum = sum - nums[left]
                left = left + 1
        
        if result != sys.maxint:
            return result
        else:
            return 0