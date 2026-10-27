class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            d[nums[i]] = i
            resultat = target - nums[i]
            if resultat in d and d[resultat] != i:               
                if i > d[resultat]:
                    return [d[resultat], i]
                return [i, d[resultat]]