class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        fre = {}

        l = 0
        maxf = 0

        for r in range(len(s)):
            fre[s[r]] = 1+ fre.get(s[r],0)
            maxf = max(maxf, fre[s[r]])

            while r-l + 1 - maxf > k:
                fre[s[l]] -= 1
                l += 1
            res = max(res, r-l + 1)
        return res
                