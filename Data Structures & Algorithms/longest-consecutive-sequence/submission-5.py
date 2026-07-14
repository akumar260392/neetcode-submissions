class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen= set(nums)
        length = 0
        for num in seen:
            if num-1 in seen:
                continue
            else:
                current_len = 1
                while num+1 in seen:
                    current_len +=1
                    num +=1
                length = max(length,current_len)
        return length
        