class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementary = {}
        for _idx, el in enumerate(nums):
            if el in complementary:
                return [complementary[el], _idx]
            complementary[target - el] = _idx