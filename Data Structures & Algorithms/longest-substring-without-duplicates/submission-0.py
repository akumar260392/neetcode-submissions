class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        stack = []
        max_length =0

        for i in s:
            if i not in stack:
                stack.append(i)
            else:
                while i in stack:
                    stack.pop(0)
                stack.append(i)
            max_length = max(max_length,len(stack))
        return max_length
        