import bisect
from collections import Counter
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        num_count = Counter(nums)
        ans = max(num_count.values())

        check_points = set(nums)
        for num in nums:
            check_points.add(num - k)
            check_points.add(num + k)

        for target in check_points:
            l = bisect.bisect_left(nums, target - k)
            r = bisect.bisect_right(nums, target + k) - 1

            elements_in_range = r - l + 1
            elements_at_target = num_count.get(target, 0)

            temp_ans = min(elements_in_range, elements_at_target + numOperations)
            ans = max(ans, temp_ans)

        return ans