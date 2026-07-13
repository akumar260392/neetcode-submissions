class Solution:
    def counter(self,s:str)->dict:
        count = {}
        for i in s:
            if i not in count:
                count[i] =1
            else:
                count[i] +=1
        return count
    def isAnagram(self, s: str, t: str) -> bool:
        return self.counter(s) == self.counter(t)

        