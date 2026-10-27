class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:      
            _ = ''.join(sorted(word))              
            d[_].append(word)

        return list(d.values())