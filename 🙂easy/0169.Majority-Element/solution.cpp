class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> m;
        for (auto & n: nums) {
            m[n]++;
        }

        for (auto p: m) {
            if (p.second > (nums.size() / 2)) {
                return p.first;
            }
        }
        return -1;
    }
};