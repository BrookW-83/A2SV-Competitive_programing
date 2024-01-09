class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map, t_map = [], []

        for i in s:
            s_map.append(s.index(i))

        for i in t:
            t_map.append(t.index(i))

        if s_map == t_map:
            return True
        return False

        
