class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        parenthesis = '('*k + ')'*k
        while s.find(parenthesis) != -1:
            s = s.replace(parenthesis, '')
        return s