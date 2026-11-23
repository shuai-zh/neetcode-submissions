class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        stack = []

        for i in intervals:
            if stack and i[0] <= stack[-1][1]:
                pre = stack.pop()
                merged = [min(pre[0],i[0]), max(pre[1],i[1])]
                stack.append(merged)
            else:
                stack.append(i)
        
        return stack