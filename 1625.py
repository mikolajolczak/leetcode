class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        visited = [False] * n
        ans = s
        s +=s
        i = 0
        while not visited[i]:
            visited[i] = True
            for j in range(10):
                if b % 2 == 0:
                    limit = 0
                else:
                    limit = 9
                for k in range(limit+1):
                    t = list(s[i:i+n])
                    for p in range(1,n,2):
                        t[p] = str((int(t[p]) + j * a)% 10)
                    for p in range(0,n,2):
                        t[p] = str((int(t[p]) + k * a)% 10)
                    t_str = ''.join(t)
                    if t_str < ans:
                        ans = t_str
            i = (i + b) % n
        return ans