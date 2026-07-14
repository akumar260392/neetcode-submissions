class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        num =1
        for i in range(1,len(nums)):
            num *= nums[i-1]
            prefix[i] = num
        
        sufix = [1]*n
        num = 1
        for i in range(len(nums)-2,-1,-1):
            num *= nums[i+1]
            sufix[i] = num

        result = []

        for i in range(len(nums)):
            val = sufix[i]*prefix[i]
            result.append(val)
        return result
        