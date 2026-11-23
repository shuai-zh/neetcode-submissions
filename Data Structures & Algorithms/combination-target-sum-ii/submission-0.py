class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        

        res = []

        def find(start, curArr, curT):
            if curT == target:
                res.append(curArr.copy())
                return
            elif curT > target:
                return
            
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    
                    continue
                curArr.append(nums[i])
                
                find(i+1, curArr, curT+nums[i])
                curArr.pop()
                
        find(0, [],0)
        return res