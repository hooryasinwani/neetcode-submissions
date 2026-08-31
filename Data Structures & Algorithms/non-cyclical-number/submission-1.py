class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = str(n)
        while True:
            res = 0
            for i in range(len(num)):
                res += int(num[i]) ** 2
            if res == 1:
                return True
            if res in seen:
                return False
            seen.add(res)
            num = str(res)
        