class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = {}
        for num in nums:
            if num in new:
                new[num] += 1
            else:
                new[num] = 1
        for val in new.values():
            if val > 1:
                return True
        return False
        