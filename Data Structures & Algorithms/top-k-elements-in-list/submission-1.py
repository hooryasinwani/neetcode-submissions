class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new = {}
        arr = []
        output = []
        for num in nums:
            if num not in new:
                new[num] = 1
            else:
                new[num]+=1

        for num, cnt in new.items():
            arr.append([cnt, num])
        arr.sort()
        while len(output)< k:
            output.append(arr.pop()[1])
        return output






















        


        # output = []
        # arr = []
        # count = {}
        # for num in nums:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        # arr.sort()
        # while len(output)< k:
        #     output.append(arr.pop()[1])
        # return output
            

      
        