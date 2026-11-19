class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_of_nums = set()
        for num in nums:
            set_of_nums.add(num)
        
        
        
        res = 1
        size = 1
        m = {}
        for num in nums:
            
            
            if num in set_of_nums:
                cur = num
                set_of_nums.remove(cur)
                while cur+1 in set_of_nums:
                    size += 1
                    cur += 1
                    set_of_nums.remove(cur)
                if cur+1 in m:
                    size += m[cur+1]
                m[num] = size
            
            res = max(res, size)
            size = 1
        
        return res
            
