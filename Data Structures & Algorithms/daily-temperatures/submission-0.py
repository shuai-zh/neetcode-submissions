class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        stack = []

        for i in range(len(temperatures)):
             
            t = temperatures[i]
            while stack and t > stack[-1][1]:
                pre_t = stack.pop()
                res[pre_t[0]] = i - pre_t[0]
            else:
                stack.append((i,t))
        return res


