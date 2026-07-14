class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen= {}

        for index,num in enumerate(numbers):
            diff= target -num
            if diff in seen:
                return [seen[diff]+1,index+1]
            seen[num] = index
        return []
        