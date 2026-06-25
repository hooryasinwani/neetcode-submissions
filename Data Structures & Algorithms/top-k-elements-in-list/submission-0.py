class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        arr = []
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        while len(output)< k:
            output.append(arr.pop()[1])
        return output
            

      
        