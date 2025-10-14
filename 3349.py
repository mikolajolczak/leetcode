from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n-2*k+1):
            first = nums[i:i+k]
            second = nums[i+k:i+2*k]
            if all(first[j] < first[j+1] for j in range(k-1)) and all(second[j] < second[j+1] for j in range(k-1)):
                return True
        return False