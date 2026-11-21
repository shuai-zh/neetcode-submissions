class TimeMap:
    
    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((timestamp, value))
            
        else:
            self.timeMap[key] = [(timestamp,value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        timestamp_list = self.timeMap[key]

        l = 0
        r = len(timestamp_list)-1
        ans = ""

        while l <= r:
            mid = (l+r)//2
            if timestamp_list[mid][0] <= timestamp:
                l = mid +1
                ans = timestamp_list[mid][1]
            elif timestamp_list[mid][0] > timestamp:
                r = mid - 1
        
            
        return ans



        
