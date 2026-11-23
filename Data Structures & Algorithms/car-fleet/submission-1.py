class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        times = []

        for i in range(len(position)):
            stack.append((position[i], speed[i]))
        
        sorted_stack = sorted(stack)

        while sorted_stack:
            cur = sorted_stack.pop()
            time = (target-cur[0])/cur[1]
            if not times or time > times[-1]:
                times.append(time)
     
        return len(times)
