class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, current):
            if start == len(s):
                res.append(current[:])
                return
            for end in range(start, len(s)):
                substring = s[start:end+1]
                if substring == substring[::-1]:
                    current.append(substring)
                    backtrack(end+1, current)
                    current.pop()
        backtrack(0, [])
        return res