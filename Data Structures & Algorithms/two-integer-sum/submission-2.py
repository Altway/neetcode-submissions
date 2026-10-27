class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):        
            resultat = target - nums[i]
            if (resultat in nums) and (i != nums.index(resultat)):
                response = [i,nums.index(resultat)]
                response.sort()
                return response
              