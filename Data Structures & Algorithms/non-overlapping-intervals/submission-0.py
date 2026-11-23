class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        res = 0

        stack = []

        for i in intervals:
            if stack and i[0] < stack[-1][1]:
                pre = stack.pop()
                res += 1
                if pre[1] < i[1]:
                    stack.append(pre)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return res
