class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _set = set()

        i = 0
        j = 0
        res = 0
        cur = 0
        while j< len(s):
            if i == j:
                cur += 1
                _set.add(s[j])
            else:
                if s[j] not in _set:
                    cur += 1
                    _set.add(s[j])
                    
                    
                else:
                    while s[i] != s[j]:
                        _set.remove(s[i])
                        i += 1
                    
                    i += 1
                    cur = j-i+1
                    
                    
            j += 1
            res = max(res, cur)
        return res
                    
