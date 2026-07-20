class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palendrom (s:str)->bool:
            left = 0
            right = len(s)-1
            while left <=right:
                if s[left] != s[right]:
                    return False
                    break
                else:
                    left +=1
                    right-=1
            return True

        if is_palendrom(s):
            return True
        else:
            for i in range(len(s)):
                string = s[:i] + s[i+1:]
                if is_palendrom(string):
                    return True
            return False
        