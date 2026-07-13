class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] =1

        # Sort the items by frequency (value) in descending order and take the first k keys
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]
        