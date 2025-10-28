from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                for direction in (1, -1):
                    copy_nums = nums.copy()
                    pos = i
                    d = direction
                    while 0 <= pos < len(copy_nums):
                        if copy_nums[pos] == 0:
                            pos += d
                        elif copy_nums[pos] > 0:
                            copy_nums[pos] -= 1
                            d *= -1
                            pos += d
                    if all(x == 0 for x in copy_nums):
                        ans += 1
        return ans