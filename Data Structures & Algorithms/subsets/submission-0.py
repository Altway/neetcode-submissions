class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        import copy
        resultat = [[]]
        for num in nums:
            _ = copy.deepcopy(resultat)
            for el in _:
                el.append(num)
                resultat.append(el)
        return resultat