class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_set = {}
        t_set = {}

        for i in range(len(s)):
            print(s[i])
            s_set[s[i]] = s_set.get(s[i], 0) + 1
            t_set[t[i]] = t_set.get(t[i], 0) + 1
        
        s_keys = s_set.keys()
        t_keys = t_set.keys()

        if s_keys == t_keys:
            for key in s_keys:
                if s_set[key] != t_set[key]:
                    return False
            return True

        return False