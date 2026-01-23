class Solution {
public:
    bool isAcronym(vector<string>& words, string s) {
        string res;
        bool find=false;
        for(auto &word : words){
                res+=word[0];
        }
        if(res==s){
            find=true;
        }
        return find;
    }
};