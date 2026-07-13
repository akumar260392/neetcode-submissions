class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] =1

        bucket = [[] for _ in range(len(nums)+1)]

        for num,count in hashmap.items():
            bucket[count].append(num)

        result = []
        for count in range(len(bucket)-1,0,-1):
            for num in bucket[count]:
                result.append(num)

                if len(result) == k:
                    return result

        
        