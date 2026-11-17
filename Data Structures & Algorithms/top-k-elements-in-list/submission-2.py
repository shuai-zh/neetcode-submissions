class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre_map = defaultdict(int)

        for num in nums:
            fre_map[num] += 1

        pq = []

        for num, fre in fre_map.items():
            
            heapq.heappush(pq,(fre,num))
            if len(pq)>k:
                heapq.heappop(pq)

        res = []
        for t in pq:
            res.append(t[1])

        return res

        

        