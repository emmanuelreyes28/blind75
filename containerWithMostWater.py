class Solution:
    def maxArea(self, height: List[int]) -> int:
        # create a pointer that starts from the left (beginning) and one that starts from the right (end)
        # track the highest value from the left and the highest value from the right but also consider the width of the container
        # result will be width times height

        # condition: check which one of the two points is smaller, then move that one respectively to the next value
        # as we iterate throught the array check which result has a greater container storage and update accordingly
        # keep going until as long as the left pointer is less than the right pointer

        result = 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] <= height[right]:
                tempResult = height[left] * (right - left)
                result = max(result, tempResult)
                left += 1
            elif height[left] >= height[right]:
                tempResult = height[right] * (right - left)
                result = max(result, tempResult)
                right -= 1
        return result
