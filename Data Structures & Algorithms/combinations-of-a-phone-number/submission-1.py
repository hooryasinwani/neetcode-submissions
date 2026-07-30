class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(start, current):
            if len(current) == len(digits):
                res.append(current[:])
                return
            for letter in phoneMap[digits[start]]:
                backtrack(start+1, current+letter)
        if digits:
            backtrack(0, "")
        return res