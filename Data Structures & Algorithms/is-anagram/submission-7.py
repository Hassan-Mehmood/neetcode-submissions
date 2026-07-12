class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_set = {}
        t_set = {}

        for x in s:
            if x not in s_set:
                s_set[x] = 0    
            s_set[x] += 1
        
        for x in t:
            if x not in t_set:
                t_set[x] = 0
            t_set[x] += 1
        
        print(f"s_set {s_set}")
        print(f"t_set {t_set}")
        s_keys = s_set.keys()
        t_keys = t_set.keys()

        if s_keys == t_keys:
            for key in s_keys:
                if s_set[key] != t_set[key]:
                    return False
            return True

        return False