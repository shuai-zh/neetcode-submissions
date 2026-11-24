class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def find(lc, rc, cur):
            if lc == rc == n:
                res.append(cur)
                return
            
            if lc < n:
                find(lc+1,rc,cur+"(")
            
            if rc < lc:
                find(lc,rc+1, cur+")")
            
        find(0,0,"")
        return res