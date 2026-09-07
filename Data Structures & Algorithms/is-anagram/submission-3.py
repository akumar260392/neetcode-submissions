class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def frequancy(s:str):
            freq = {}

            for i in s:
                if i in freq:
                    freq[i] +=1
                else:
                    freq[i] =1
            return freq
        return frequancy(s) == frequancy(t)
        