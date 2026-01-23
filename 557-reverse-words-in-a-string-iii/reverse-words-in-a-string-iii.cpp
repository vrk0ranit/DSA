class Solution {
public:
    string reverseWords(string s) {
        string temp="";
        string res="";
        for(int i=0;i<s.size();i++){
            if(s[i]==' '){
                for(int j=temp.size()-1;j>=0;j--){
                    res+=temp[j];
                }
                res+=' ';
                temp="";
            }else{
                temp+=s[i];
            }
        }
        for (int j = temp.size() - 1; j >= 0; j--) {
            res += temp[j];
        }
        return res;
    }
};