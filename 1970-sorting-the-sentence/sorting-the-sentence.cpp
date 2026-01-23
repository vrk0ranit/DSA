class Solution {
public:
    string sortSentence(string s) {
       string res="";
       vector<string> words(10);
       string temp="";
       for(int i=0;i<=s.size();i++){
        if(i==s.size() || s[i]==' '){
            int pos=temp.back()-'0';
            temp.pop_back();
            words[pos]=temp;
            temp="";
        }else{
            temp+=s[i];
        }
       }
       for(int i=0;i<words.size();i++){
        if(!words[i].empty()){
            if(!res.empty()) res+= " ";
            res+=words[i];
        }
       }
       return res;
    }
};