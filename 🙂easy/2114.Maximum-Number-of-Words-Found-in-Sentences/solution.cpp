class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int res = 0;
        for (auto& s: sentences) {
            int n = 0;
            for (int i =0; i<s.size();i++) {
                if (s[i] == ' ') n++;
            }
            res = max(n, res);
        }
        return res+1;
    }
};