class Solution {
public:
    string toLowerCase(string s) {
        string res=s;
        for(int i=0;i<s.size();i++){
            if(res[i]>='A' && res[i]<='Z'){
                res[i]=res[i]+32;
            }
        }
        return res;
    }
};