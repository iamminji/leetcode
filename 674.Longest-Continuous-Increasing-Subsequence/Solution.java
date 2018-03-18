/*
    674. Longest Continuous Increasing Subsequence
    https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
*/


class Solution {
    public int findLengthOfLCIS(int[] nums) {

        int[] dp = new int[nums.length];
        for (int i = 0; i < nums.length; ++i) {
            dp[i] = 1;
        }

        for (int i = 1; i < nums.length; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] > nums[j]) {
                    dp[i] = dp[j] + 1;
                } else {
                    dp[i] = 1;
                }
            }
        }
        int max = 0;
        for (int i = 0; i < dp.length; ++i) {
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}
