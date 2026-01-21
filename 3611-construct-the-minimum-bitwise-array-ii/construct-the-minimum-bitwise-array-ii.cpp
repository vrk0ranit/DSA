class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        int n=nums.size();
        vector<int> ans(n);
        for(int idx=0;idx<n;idx++){
            int i=nums[idx];
            if(i%2==0){
                ans[idx]=-1;
            }else{
                int x=i+1;
                int lowbit=x & -x;
                ans[idx]=i-(lowbit>>1);
            }
        }
        return ans;
    }
};