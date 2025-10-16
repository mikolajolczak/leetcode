from collections import Counter
from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counts = Counter(num% value for num in nums)
        i = 0
        while True:
            if counts[i%value] == 0:
                return i
            counts[i%value] -= 1
            i += 1