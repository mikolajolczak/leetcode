from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        if n == 0 or m == 0:
            return 0

        prefix_skill = [0] * (n + 1)
        for i in range(n):
            prefix_skill[i + 1] = prefix_skill[i] + skill[i]

        start_prev = 0
        start_time = 0

        for j in range(m):
            if j == 0:
                start_time = 0
            else:
                min_start = 0
                current_time_prev = start_prev
                work_prev = skill[0] * mana[j - 1]
                finish_prev = current_time_prev + work_prev
                min_start = max(min_start, finish_prev)
                current_time_prev = finish_prev

                for wizard in range(1, n):
                    work_time_prev = skill[wizard] * mana[j - 1]
                    finish_prev = current_time_prev + work_time_prev

                    time_to_reach = prefix_skill[wizard] * mana[j]

                    min_start = max(min_start, finish_prev - time_to_reach)
                    current_time_prev = finish_prev

                start_time = min_start

            start_prev = start_time

        total_time = start_time
        for wizard in range(n):
            total_time += skill[wizard] * mana[m - 1]

        return total_time