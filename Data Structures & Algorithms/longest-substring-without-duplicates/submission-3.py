class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _set = set()

        i = 0
        j = 0
        res = 0
        
        while j< len(s):
            while s[j] in _set:
                _set.remove(s[i])
                i += 1
            _set.add(s[j])       
            
            res = max(res, j-i+1)
            j += 1
        return res
                    
