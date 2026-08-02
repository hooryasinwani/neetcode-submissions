class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_1 = {}
        count_2 = {}
        left = 0
        for i in range(len(s1)):
            count_1[s1[i]] = count_1.get(s1[i], 0)+1
        for right in range(len(s2)):
            count_2[s2[right]]= count_2.get(s2[right], 0)+1
            if (right-left+1) > len(s1):
                count_2[s2[left]]-=1
                if count_2[s2[left]] == 0:
                    del count_2[s2[left]]
                left +=1
            if count_1 == count_2:
                return True
        return False
        


    
        