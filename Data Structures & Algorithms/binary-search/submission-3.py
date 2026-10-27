class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        _idx = (i + j)//2
        visited = set()
        while nums[_idx] not in visited:
            visited.add(nums[_idx])
            #print(visited)
            if nums[_idx] == target:
                return _idx
            elif nums[_idx] > target:
                j = _idx
            elif nums[_idx] < target:
                i = _idx
            _idx = (i + j)//2
        return -1