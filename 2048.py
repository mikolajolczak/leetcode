class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(num:int) -> bool:
            s = str(num)
            count = {}
            for digit in s:
                count[digit] = count.get(digit, 0) + 1
            for digit, freq in count.items():
                if int(digit) != freq:
                    return False

            return True

        candidate = n + 1
        while True:
            if is_balanced(candidate):
                return candidate
            candidate += 1
