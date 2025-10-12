from typing import List

class Solution:

    @staticmethod
    def precomputeFactorials(maxn, MOD):
        fact = [1] * (maxn + 1)
        invfact = [1] * (maxn + 1)
        for i in range(1, maxn + 1):
            fact[i] = fact[i - 1] * i % MOD
        invfact[maxn] = pow(fact[maxn], MOD - 2, MOD)
        for i in range(maxn, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD
        return fact, invfact

    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        fact, invfact = self.precomputeFactorials(m, MOD)
        pow_nums = [[1] * (m + 1) for _ in range(n)]
        for j in range(n):
            for t in range(1, m + 1):
                pow_nums[j][t] = (pow_nums[j][t - 1] * nums[j]) % MOD
        dp = {(0, 0): [1] + [0] * m}
        for j in range(n):
            next_dp = {}
            for (carry, ones), poly in dp.items():
                for t in range(0, m + 1):
                    val_t = pow_nums[j][t] * invfact[t] % MOD
                    ssum = carry + t
                    bit = ssum & 1
                    carry2 = ssum >> 1
                    ones2 = ones + bit
                    if ones2 > k:
                        continue

                    key = (carry2, ones2)
                    if key not in next_dp:
                        next_dp[key] = [0] * (m + 1)
                    tgt = next_dp[key]

                    if val_t == 0:
                        continue
                    lim = m - t
                    mod = MOD
                    for s in range(lim + 1):
                        coeff = poly[s]
                        if coeff:
                            tgt[s + t] = (tgt[s + t] + coeff * val_t) % mod

            dp = next_dp

        result_a = 0
        for (carry, ones), poly in dp.items():
            total_ones = ones + bin(carry).count('1')
            if total_ones == k:
                result_a = (result_a + poly[m]) % MOD

        return result_a * fact[m] % MOD