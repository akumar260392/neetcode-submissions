class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = sorted(zip(position,speed),reverse=True)

        stack = []

        for pos,spd in car:
            time = (target-pos)/spd

            if stack and time <= stack[-1]:
                continue
            
            stack.append(time)
        return len(stack)
        