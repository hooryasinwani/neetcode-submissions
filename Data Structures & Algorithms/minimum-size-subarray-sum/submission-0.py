class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        _sum = 0
        res = len(nums)+1
        for right in range(len(nums)):
            _sum += nums[right]
            while _sum >= target:
                res = min(res, right-left+1)
                _sum-= nums[left]
                left +=1
        if res == len(nums)+1:
            return 0
        else:
            return res

    
        