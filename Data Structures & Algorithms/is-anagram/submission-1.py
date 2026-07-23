class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counter(s:str)->dict:
            res={}
            for i in s:
                if i in res:
                    res[i] +=1
                else:
                    res[i] = 1
            return res
        
        return counter(s) == counter(t)