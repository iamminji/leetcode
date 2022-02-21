class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int res = 0;
        for (auto& s: operations) {
            if (s[0] == '-' || s[2] == '-') {
                res -= 1;
            } else {
                res += 1;
            }
        }
        return res;
    }
};