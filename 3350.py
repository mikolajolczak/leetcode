from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        inc = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc[i] = inc[i + 1] + 1

        left, right = 1, n // 2
        ans = 0

        def hasIncreasingSubarrays(k: int) -> bool:
            for i in range(n - 2 * k + 1):
                if inc[i] >= k and inc[i + k] >= k:
                    return True
            return False

        while left <= right:
            mid = (left + right) // 2
            if hasIncreasingSubarrays(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans