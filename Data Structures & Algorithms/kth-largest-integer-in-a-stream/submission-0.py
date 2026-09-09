from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        # Build min heap
        self.heap(self.nums, "min")

        # Keep only k largest elements
        while len(self.nums) > self.k:
            self._remove_root()

    @staticmethod
    def _heapify(nums: list, n: int, i: int, heap_type: str):
        while True:
            target = i

            left = 2 * i + 1
            right = 2 * i + 2

            if heap_type == "max":
                if left < n and nums[left] > nums[target]:
                    target = left

                if right < n and nums[right] > nums[target]:
                    target = right

            elif heap_type == "min":
                if left < n and nums[left] < nums[target]:
                    target = left

                if right < n and nums[right] < nums[target]:
                    target = right

            if target == i:
                break

            nums[i], nums[target] = nums[target], nums[i]
            i = target

    @staticmethod
    def heap(nums,heap_type):
        n = len(nums)

        for i in range((n // 2) - 1, -1, -1):
            KthLargest._heapify(nums, n, i, heap_type)

        return nums

    def _remove_root(self):
        n = len(self.nums)

        if n == 0:
            return

        # Move last element to root
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]

        # Remove old root
        self.nums.pop()

        # Heapify down
        if self.nums:
            self._heapify(self.nums, len(self.nums), 0, "min")

    def add(self, val: int) -> int:

        self.nums.append(val)

        # Rebuild min heap
        self.heap(self.nums, "min")

        # Keep only k elements
        while len(self.nums) > self.k:
            self._remove_root()

        return self.nums[0]
