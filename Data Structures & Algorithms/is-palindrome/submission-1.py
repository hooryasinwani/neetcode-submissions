class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False

        