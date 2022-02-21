class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> result = {};
        int index = 0;
        for (auto &n: nums) {
            result.push_back(nums[nums[index++]]);
        }
        return result;
    }
};