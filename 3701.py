from typing import List

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                ans+=num
            else:
                ans-=num
        return ans