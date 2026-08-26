class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        isEnd = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if i ==isEnd:
                jumps+=1
                isEnd = farthest
        return jumps
