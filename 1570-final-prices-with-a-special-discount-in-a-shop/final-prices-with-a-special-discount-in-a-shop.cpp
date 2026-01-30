class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        int n=prices.size();
        vector<int> res(n);
        for(int i=0;i<n;i++){
            res[i]=prices[i];
            for(int j=i+1;j<n;j++){
                if(j>i && prices[j]<=prices[i]){
                    res[i]=prices[i]-prices[j];
                    break;
                }
            }
        }
        return res;
    }
};