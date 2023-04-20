class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:  # means it is already sorted
                # find the min between current result and leftmost value
                result = min(result, nums[left])
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[left]:
                # search on the right side for min value
                left = mid + 1
            else:
                # search obn the left side for min value
                right = mid - 1

        return result
