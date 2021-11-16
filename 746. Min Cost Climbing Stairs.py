class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 2)
        #dp[2] = cost[1];
        for i in range(2, n + 1):
            dp[i + 1] = min(dp[i - 1] + cost[i - 2], dp[i] + cost[i - 1])
            
        return dp[n + 1]
        
        
