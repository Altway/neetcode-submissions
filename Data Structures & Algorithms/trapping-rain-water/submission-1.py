class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        response = 0
        max_left = height[i]
        max_right = height[j]
        while i<j:           
            if height[i] <= height[j]:
                i += 1
                max_left = max(max_left, height[i])
                response += max_left - height[i]
            else:
                j -= 1
                max_right = max(max_right, height[j])
                response += max_right - height[j]

        return response