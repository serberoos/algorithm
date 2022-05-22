# Find Pivot Index | sliding :: 724

피봇이란 피봇 왼쪽의 숫자들의 합과  피봇 오른쪽의 합이 같은 자리가 피봇이다.

- 문제

피봇을 찾아서 인덱스를 리턴하고 피봇이 없을 경우 -1을 리턴하라.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/76563108-6caf-47d3-8118-31106897509a/Untitled.png)

sliding 개념을 이용해야함

---

brute force 방법 - 조합가능한 경우를 모두 대입해본다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/329b2baf-07b7-4273-92ff-c0f883001b9f/Untitled.png)

처음부터 index를 증가시키면서 왼쪽과 오른쪽을 다 더해 pivot을 찾아낸다.

⇒ O(n) + O(n) ... = O(n) x n = O(n^2)이 된다.

---

### Solution

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4a2c9c8a-932b-4ee8-97ef-d03619eabd6d/Untitled.png)

- sliding 방법

피봇이 한칸씩 움직 일때 마다 right sum에서 해당 숫자를 빼주고 left sum에 한턴 전의 숫자를 더해 줘 left sum과 right sum 이 같아 지는 곳이 pivot이다.

- 참고 사항

모든 숫자가 양수일 경우에만 알고리즘을 사용할 수 있다.

---

## Implementation

LeetCode 724. Find Pivot Index

- python

```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pastPivotNum = 0
        pivotIndex = 0
        leftSum = 0
        rightSum = sum(nums)
        
        while pivotIndex < len(nums):
            pivot = nums[pivotIndex]
            
            leftSum = leftSum + pastPivotNum
            rightSum = rightSum -pivot
            
            if(leftSum == rightSum):
                return pivotIndex
            
            pivotIndex = pivotIndex + 1
            pastPivotNum = pivot
				return -1
```