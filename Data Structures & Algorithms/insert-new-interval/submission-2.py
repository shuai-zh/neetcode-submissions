class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        stack = []
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if newInterval[0] > interval[1]:
                stack.append(interval)
                i += 1
            else:
                if newInterval[1] < interval[0]:
                    stack.append(newInterval)
                    stack.append(interval)
                    for j in range(i+1, len(intervals)):
                        stack.append(intervals[j])
                    
                else:
                    interval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
                    stack.append(interval)
                    for j in range(i+1, len(intervals)):
                        cur = stack[-1]
                        interval = intervals[j]
                        if cur[1] < intervals[j][0]:
                            stack.append(intervals[j])
                        else:
                            stack.pop()
                            interval = [min(interval[0], cur[0]), max(interval[1], cur[1])]
                            stack.append(interval)
                break    
        return stack