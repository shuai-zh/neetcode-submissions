class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [0] *len(nums)

        res = []

        def collect(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            

            for i in range(len(nums)):
                if visited[i] == 0:
                    cur.append(nums[i])
                    visited[i] = 1
                    collect(cur)
                    cur.pop()
                    visited[i] = 0
                else:
                    continue
        
        collect([])
        return res