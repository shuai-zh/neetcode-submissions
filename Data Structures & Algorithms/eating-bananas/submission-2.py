class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canFinish(k, piles):
            h = 0
            for pile in piles:
                h = h + math.ceil(pile/k)
            
            return h
        upper = max(piles)
        lower = 1
        res = upper
        found = False

        while lower <= upper:
            mid = (upper+lower)//2 
            cur = canFinish(mid, piles)
            

            if cur <= h:
                res = min(res, mid)
                
                upper = mid -1
                found = True
            else:
                lower = mid +1
                
        return res


        

        