impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::with_capacity(nums.len());
        for i in 0..nums.len() as usize {
            result.push(nums[nums[i] as usize]);
        }
        result
    }
}
