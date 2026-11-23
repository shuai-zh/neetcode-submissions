class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        

        def rSet(start, cur):
            if start >= len(nums):
                return
            
            arr = cur.copy()
            res.append(arr)

            for i in range(start+1, len(nums)):
                cur.append(nums[i])
                rSet(i, cur)
                cur.pop()
        
        rSet(-1,[])
        return res
