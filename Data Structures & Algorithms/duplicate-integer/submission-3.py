class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for el in nums:
            if el in visited:
                return True
            visited.add(el)
        return False