class Solution {
public:
    int minimumCost(vector<int>& nums) {
        int n=nums.size();
        int minSum=INT_MAX;
        for(int i=0;i<n-2;i++){
            for(int j=i+1;j<n-1;j++){
               vector<int> A(nums.begin(), nums.begin()+i+1); 
               vector<int> B(nums.begin()+i+1, nums.begin()+j+1);
               vector<int> C(nums.begin()+j+1, nums.end());
               int sum=A[0]+B[0]+C[0];
               minSum=min(sum,minSum);
            }
        }
        return minSum;
    }
};