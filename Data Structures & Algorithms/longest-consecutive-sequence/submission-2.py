class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        neighborhood = set(nums)
        response = 1
        for num in neighborhood:
            if num-1 not in neighborhood:
                current_list_len = 0
                i = num            
                while i in neighborhood:
                    current_list_len += 1
                    i += 1
                response = max(current_list_len, response)

        return response