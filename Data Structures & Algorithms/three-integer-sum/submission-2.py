class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(temp))
        result = []
        for i in res:
            result.append(list(i))
        return result
#     set() ensures all triplets are unique

# tuple() allows adding lists to a set (because tuples are immutable)

# Later, you convert back to list to match return type requirements
        
        