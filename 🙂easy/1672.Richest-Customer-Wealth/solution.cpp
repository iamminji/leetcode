class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int res = -1;
        for (auto& row: accounts) {
            int sum = 0;
            for (auto& col: row) {
                sum += col;
            }
            res = max(res, sum);
        }
        return res;
    }
};