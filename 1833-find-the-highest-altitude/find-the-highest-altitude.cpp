class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int n=gain.size();
        vector<int> altitudes(n+1);
        int start=0;
        altitudes[0]=start;
        int highAlt=altitudes[0];  
        for(int i=1;i<=n;i++){
            altitudes[i]=altitudes[i-1]+gain[i-1];
            highAlt=max(highAlt, altitudes[i]);
        }
        return highAlt;
    }
};