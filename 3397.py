from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        next_free = float('-inf')

        for x in nums:
            value = max(x - k, next_free)

            if value <= x + k:
                count += 1
                next_free = value + 1

        return count