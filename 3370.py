class Solution:
    def smallestNumber(self, n: int) -> int:
        i = 0
        while 2 ** i - 1 < n:
            i +=1
        return 2 ** i - 1
