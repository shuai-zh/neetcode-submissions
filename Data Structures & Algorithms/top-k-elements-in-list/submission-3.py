class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre_map = defaultdict(int)

        for num in nums:
            fre_map[num] += 1

        buckets = [[] for i in range(len(nums)+1)]

        for n,f in fre_map.items():
            buckets[f].append(n)
        res = []
        for i in range(len(buckets)-1,0,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
