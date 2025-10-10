from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        prefixes = [0 for _ in range(k)]
        for i in range(k):
            j = i
            while j<len(energy):
                prefixes[i] += energy[j]
                j+=k
        max_energy = float('-inf')
        for i in range(len(energy)):
            idx = i%k
            max_energy = max(max_energy, prefixes[idx])
            prefixes[idx] -= energy[i]

        return max_energy