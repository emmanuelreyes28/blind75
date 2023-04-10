class Solution:
    # O(n) time | O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        '''
        store the cheapest stock price availble and sell it on any future date for a max profit

        find the lowest value in the array
        find the highest value in the array thereafter

        take the difference from highest and lowest and store as profit value
        '''

        left, right = 0, 1  # left is buy, right is sell
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:  # theres a profit
                profit = prices[right] - prices[left]  # calculate profit
                maxProfit = max(maxProfit, profit)  # update maxProfit
            else:
                left = right  # since right will be the lowest value at this point
            right += 1
        return maxProfit
