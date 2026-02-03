class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int n=nums.size();
        if(n<4) return false;
        int i=0;
        while(i+1<n && nums[i]<nums[i+1]) i++;
        if(i==0) return false;
        int mid=i;
        while(i+1<n && nums[i]>nums[i+1]) i++;
        if(mid==i) return false;
        int mid2=i;
        while(i+1<n && nums[i]<nums[i+1]) i++;
        return i==n-1 && mid2<n-1;
    }
};