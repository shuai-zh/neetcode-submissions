class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        
        for word in strs:
            char_array = [0] * 26

            for char in word:
                char_num = ord(char) - ord("a")
                char_array[char_num] += 1
            
            tupled_arr = tuple(char_array)
            
            if tupled_arr in str_map:
                str_map[tupled_arr].append(word)
            else:
                str_map[tupled_arr] = [word]
        
        return list(str_map.values())
