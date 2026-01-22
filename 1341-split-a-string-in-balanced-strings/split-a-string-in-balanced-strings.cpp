class Solution {
public:
    int balancedStringSplit(string s) {
        int count=0;
        int Rcount=0;
        int Lcount=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='R'){
                Rcount++;
            }else if(s[i]=='L'){
                Lcount++;
            }
            if(Rcount==Lcount){
                count++;
            }
        }
        return count;
    }
};