class Solution:
    # O(n) time | O(n) space
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Get the product of values to the left of index position and same for the values to the right. We will be using a default of 1 for both prefix and postfix and updating these vars repestively as we iterate through the array. Afterwards, multiply the prefix and postfix values together to get the expected result for each index position.
        '''
        result = [1 for _ in range(len(nums))]

        prefix = 1
        # left to right
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        # right to left
        postfix = 1
        for i in reversed(range(len(nums))):
            result[i] *= postfix
            postfix *= nums[i]
        return result
