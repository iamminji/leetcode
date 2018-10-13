/*
    746. Min Cost Climbing Stairs
    https://leetcode.com/problems/min-cost-climbing-stairs/description/
*/


public class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] dp = new int[cost.length];
        dp[0] = cost[0];
        dp[1] = cost[1];

        if (cost.length <= 2) {
            return Math.min(dp[0], dp[1]);
        }

        for (int i = 2; i < cost.length; ++i) {
            dp[i] = Math.min(dp[i - 1] + cost[i], dp[i - 2] + cost[i]);
        }

        return Math.min(dp[cost.length - 1], dp[cost.length - 2]);
    }

}