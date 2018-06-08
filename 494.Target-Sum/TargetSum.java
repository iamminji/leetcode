/**
 * 494. Target Sum
 * https://leetcode.com/problems/target-sum/description/
 */

public class TargetSum {

    public int dfs(int i, int[] nums, int result, int target){
        if (i >= nums.length) {
            return result == target ? 1:0;
        }

        int temp = 0;
        temp += dfs(i+1, nums, result + nums[i], target);
        temp += dfs(i+1, nums, result - nums[i], target);

        return temp;
    }

    public int findTargetSumWays(int[] nums, int S) {
        int result = 0;
        result += dfs(0, nums, 0, S);
        return result;
    }
}