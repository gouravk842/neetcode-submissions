class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        right , left = 0,0
        while True:
            if left>=len(prices) or right>=len(prices):
                break
            profit = prices[right]-prices[left]
            max_profit = profit if profit>max_profit else max_profit

            if prices[left]>prices[right]:
                left+=1
            else:
                right+=1
        return max_profit
            

        