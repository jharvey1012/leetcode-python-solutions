# Top Down With Recursion + Memoization
class Solution:
    memo = {}
    
    def climbStairs(self, n: int) -> int:
        # On the first step the are two choices if n > 1, you can climb 1 step or you can climb 2 steps
        # If you climb one step, go there, and see how many ways there are to climb up from there and just minus 1 from the steps you've taken
        
        # if you climb two stairs, just go there and minus 2 from n
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.memo[n]




# BOTTOM-UP DP:
class Solution:
    memo = {}
    
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        
        for i in range(n+1):
            if i == 0 or i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
                