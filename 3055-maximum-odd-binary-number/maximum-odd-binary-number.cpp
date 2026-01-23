class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int ones=0;
        for(char ch : s){
            if(ch=='1'){
                ones++;
            }
        }
        return string(ones-1,'1')+string(s.size()-ones,'0')+ '1';
    }
};