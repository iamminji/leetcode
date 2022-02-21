class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> res(n * 2);
        for(int i=0,j=0;i<n*2;i+=2) {
            res[i] = nums[j++];
        }
        for (int i=1,j=0; i<n*2;i+=2) {
            res[i] = nums[n+(j++)];
        }
        return res;
    }
};