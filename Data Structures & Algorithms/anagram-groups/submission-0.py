class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)
        for word in strs:
            s_word = sorted(word)
            key = ''.join(s_word)
            _dict[key].append(word)
        return list(_dict.values())
   


            
                

            
        
        

        
        