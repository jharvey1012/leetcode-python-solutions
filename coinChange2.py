class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)  # intialize our dp "matrix" (just need a single array here tho)
        dp[0] = 1 # if you want to make the amount 0 there is one way (use no coins)

        for coin in coins:
            for i in range(1, amount+1):
                if i >= coin:
                    dp[i] += dp[i-coin]
        return dp[-1]