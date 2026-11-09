class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        response = 0
        while i<=j:       
            response = max(response, abs(j-i)*min(heights[i], heights[j]))
            if heights[i] > heights[j]:
                j -= 1
                continue
            i += 1

        return response