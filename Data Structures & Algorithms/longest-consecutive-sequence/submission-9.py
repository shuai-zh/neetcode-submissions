class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_of_nums = set()
        for num in nums:
            set_of_nums.add(num)
        
        
        
        res = 1
        size = 1
        
        for num in nums: 
            if num-1 not in set_of_nums:
                cur = num
                
                while cur+1 in set_of_nums:
                    size += 1
                    cur += 1
                
            
            res = max(res, size)
            size = 1
        
        return res
            
