from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        return max(frequency,key=frequency.get)
        