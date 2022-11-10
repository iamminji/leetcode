impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut result = Vec::new();
        for i in 0..2 {
            for num in &nums {
                result.push(*num);
            }
        }
        result
    }
}
