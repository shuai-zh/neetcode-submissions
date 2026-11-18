class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        size = []
        for s in strs:
            size.append(str(len(s)))
        
        return ",".join(size)+"#"+"".join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        index = s.find("#")
        size_str = s[0:index]
        char_str = s[index+1:]

        size = size_str.split(",")
        i = 0
        res = []
        for l in size:
            res.append(char_str[i: i+int(l)])
            i += int(l)
        return res




            
        