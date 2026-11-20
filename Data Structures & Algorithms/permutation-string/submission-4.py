class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        m = defaultdict(int)

        for char in s1:
            m[char] += 1

    

        while r < len(s2):
            if s2[r] not in m:
                while l < r:
                    m[s2[l]] += 1
                    l += 1
                l = r+1
                
                
                 
            elif s2[r] in m and m[s2[r]] > 0:
                m[s2[r]] -= 1
                
                
                if r-l+1 == len(s1):
                    return True
            else:
                
                while l < r:
                    if s2[l] != s2[r]:
                        m[s2[l]] += 1
                        
                        l += 1
                    else:
                        l += 1
                        break
                
            r += 1      
                
        return False

