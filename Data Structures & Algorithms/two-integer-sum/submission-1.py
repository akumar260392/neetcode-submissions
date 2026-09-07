class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for k,v in enumerate(nums):
            required = target-v
            if required in seen:
                return [seen[required],k]
            else:
                seen[v] = k
        