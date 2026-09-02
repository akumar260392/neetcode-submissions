class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <=1 :
            return False
        v = {")":"(","]":"[","}":"{"}
        valid = []
        for p in s:
            if p in "({[":
                valid.append(p)
            else:
                if not valid or v[p] != valid[-1]:
                    return False
                valid.pop()
            
        return len(valid)==0
        