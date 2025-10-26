class Solution:
    def totalMoney(self, n: int) -> int:
        last_i = 0
        total = 0
        last_day = 0
        for i in range(n):
            if i % 7 == 0:
                last_i = last_i + 1
                total += last_i
            elif i % 7 == 1:
                last_day = last_i + 1
                total += last_day
            else:
                last_day = last_day + 1
                total += last_day
        return total




if __name__ == '__main__':
    s = Solution()
    print(s.totalMoney(20))