/*
    503. Next Greater Element II
    https://leetcode.com/problems/next-greater-element-ii/
*/


public class NextGreaterElement2 {
    public int[] nextGreaterElements(int[] nums) {

        int[] answer = new int[nums.length];
        Arrays.fill(answer, -1);
        Stack<Integer> stack = new Stack<>();


        for (int i = nums.length * 2 - 1; i >= 0; i--) {
            while (!stack.empty() && nums[i % nums.length] >= stack.peek()) {
                stack.pop();
            }
            if (!stack.empty()) {
                answer[i % nums.length] = stack.peek();
            }
            stack.push(nums[i % nums.length]);
        }

        return answer;
    }
}