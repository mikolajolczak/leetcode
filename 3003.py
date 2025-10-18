class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        left = [[0, 0, 0] for _ in range(n)]
        right = [[0, 0, 0] for _ in range(n)]

        num = mask = count = 0
        for i in range(n - 1):
            bit = 1 << (ord(s[i]) - ord("a"))
            if not (mask & bit):
                count += 1
                if count <= k:
                    mask |= bit
                else:
                    num += 1
                    mask = bit
                    count = 1
            left[i + 1] = [num, mask, count]

        num = mask = count = 0
        for i in range(n - 1, 0, -1):
            bit = 1 << (ord(s[i]) - ord("a"))
            if not (mask & bit):
                count += 1
                if count <= k:
                    mask |= bit
                else:
                    num += 1
                    mask = bit
                    count = 1
            right[i - 1] = [num, mask, count]

        max_val = 0
        for i in range(n):
            seg = left[i][0] + right[i][0] + 2

            combined_mask = left[i][1] | right[i][1]
            combined_count = bin(combined_mask).count("1")

            if left[i][2] == k and right[i][2] == k and combined_count < 26:
                seg += 1
            elif min(combined_count + 1, 26) <= k:
                seg -= 1

            max_val = max(max_val, seg)

        return max_val