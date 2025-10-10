from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        all_zero = True
        for num in nums:
            ans ^= num
            if num != 0:
                all_zero = False
        if all_zero:
            return 0
        if ans != 0:
            return len(nums)
        return len(nums) - 1