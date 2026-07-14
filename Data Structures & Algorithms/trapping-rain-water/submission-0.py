class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right_wall = left_wall =0
        r_max = [0]*n
        l_max = [0]*n

        for i in range(n):
            j = -i -1
            r_max[j] = right_wall
            l_max[i] = left_wall
            right_wall = max(right_wall,height[j])
            left_wall = max(left_wall,height[i])

        water = 0

        for i in range(n):
            pot = min(r_max[i],l_max[i])
            water += max(0,pot-height[i])
        return water




            

        