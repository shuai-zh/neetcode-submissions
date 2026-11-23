class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        def find(start, curArr, curT):
            if curT == target:
                res.append(curArr.copy())
                return
            elif curT > target:
                return
            
            for i in range(start,len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                curArr.append(nums[i])
                find(i, curArr, curT+nums[i])
                curArr.pop()
        find(0, [],0)
        return res
            

            