class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_new = sorted(s)
        t_new = sorted(t)
        return s_new == t_new
        

        

        
            

        