class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = [0] * len(nums)
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue #skip this
                prod *= nums[j]
            new[i] = prod
        return new
        