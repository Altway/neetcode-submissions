class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        sorted_nums = sorted(nums)
        response = set()
        while i < len(nums):
            target = -sorted_nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                two_sum = sorted_nums[j] + sorted_nums[k]
                if two_sum < target:
                    j += 1
                    continue
                if two_sum > target:
                    k -= 1
                    continue
                if two_sum == target:
                    response.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
                    
            i += 1

        return list(response)

         