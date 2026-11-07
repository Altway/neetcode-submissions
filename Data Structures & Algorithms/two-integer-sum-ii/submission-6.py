class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bsearch(idx, number, arr):
            l = idx
            r = len(arr)
            while r - l > 1:
                anchor = (r+l)//2
                if arr[anchor] < number:
                    l = anchor
                elif arr[anchor] > number:
                    r = anchor
                else:
                    return anchor
            return None
        i = 0
        while i != len(numbers):
            idx_target = bsearch(i,target-numbers[i], numbers)
            if idx_target:
                return [i+1, idx_target+1]
            i += 1
