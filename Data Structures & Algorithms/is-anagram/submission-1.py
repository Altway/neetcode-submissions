class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ctr = defaultdict(int)
        t_ctr = defaultdict(int)
        for letter in s:
            s_ctr[letter] += 1
        for letter in t:
            t_ctr[letter] += 1
        return s_ctr == t_ctr
