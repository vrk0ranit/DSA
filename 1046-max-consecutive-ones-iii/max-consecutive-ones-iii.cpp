class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int j=0;
        int maxLength=0;
        int zeroCount=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                zeroCount++;
            }
            while(zeroCount>k){
                if(nums[j]==0){
                    zeroCount--;
                }
                j++;
            }
            maxLength=max(maxLength, i-j+1);
        }
        return maxLength;
    }
};