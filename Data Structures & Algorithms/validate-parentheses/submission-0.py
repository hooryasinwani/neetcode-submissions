class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}": "{", ")": "(", "]":"["}
        stack = []
        for char in s:
            if char in pairs.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if pairs[char] != last:
                    return False
        return not stack
        