class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word;
        string res="";
        while(ss >> word){
            if(!res.empty()){
                res=word+" "+res;
            }else{
                res=word;
            }
        }
        return res;
    }
};