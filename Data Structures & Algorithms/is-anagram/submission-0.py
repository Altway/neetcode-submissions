class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ctr = Counter(s)
        t_ctr = Counter(t)
        return s_ctr == t_ctr
        