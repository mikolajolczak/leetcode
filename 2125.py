from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        i=0
        while i < len(bank):
            if '1' in bank[i]:
                for j in range(i+1, len(bank)):
                    if '1' in bank[j]:
                        ans += bank[i].count('1') * bank[j].count('1')
                        break
            i += 1
        return ans