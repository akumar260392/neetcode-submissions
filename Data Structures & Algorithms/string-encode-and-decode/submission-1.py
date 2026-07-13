class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for char in strs:
            result += str(len(char))+"#"+char
        return result

    def decode(self, s: str) -> List[str]:

        result = []
        
        char = ""
        
        num = 0
        i = len(s)
        j  = 0
        
        while j < i:
            if s[j].isdigit():
                num = num*10+int(s[j])
                j +=1
            elif s[j] == "#":
                j += 1
                char = s[j:j+num]
                result.append(char)
                j += num
                char = ""
                num = 0
            else:
                j+=1
        return result

