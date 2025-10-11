import bisect
from typing import List
from collections import Counter

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0

        cnt = Counter(power)
        vals = sorted(cnt)
        gains = [v * cnt[v] for v in vals]
        n = len(vals)
        dp = [0] * n

        for i in range(n):
            gain = gains[i]
            prev = bisect.bisect_right(vals, vals[i] - 3) - 1
            take = gain + (dp[prev] if prev >= 0 else 0)
            not_take = dp[i - 1] if i > 0 else 0
            dp[i] = max(not_take, take)

        return dp[-1]