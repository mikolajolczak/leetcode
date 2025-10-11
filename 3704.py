from functools import lru_cache


class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        digits = list(map(int, str(n)))[::-1]
        L = len(digits)
        ans = 0

        for la in range(1, L + 1):
            for lb in range(1, L + 1):
                @lru_cache(None)
                def dp(pos: int, carry: int) -> int:
                    if pos == L:
                        return 1 if carry == 0 else 0
                    ways = 0
                    target = digits[pos]
                    da_iter = range(1, 10) if pos < la else (0,)
                    db_iter = range(1, 10) if pos < lb else (0,)
                    for da in da_iter:
                        for db in db_iter:
                            ssum = da + db + carry
                            if ssum % 10 == target:
                                ways += dp(pos + 1, ssum // 10)
                    return ways

                ans += dp(0, 0)

        return ans