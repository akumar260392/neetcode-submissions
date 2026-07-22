class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if s == "" or t == "":
            return ""
        needmap = Counter(t)
        need = len(needmap)

        window = {}
        have = 0
        l =0
        result = ""
        min_length = float('inf')


        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch,0) + 1
            
            if ch in needmap and window[ch] == needmap[ch]:
                have +=1
            while have == need:
                if (r-l+1) < min_length:
                    min_length = r-l+1
                    result = s[l:r+1]
                window[s[l]] -=1
                
                if s[l] in needmap and window[s[l]] < needmap[s[l]]:
                    have -=1
                l +=1
        return result

        