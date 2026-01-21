class Solution {
public:
    string reversePrefix(string word, char ch) {
        string s,s1,s2;
        for(int i=0;i<word.size();i++){
            if(word[i]==ch){
                s1=word.substr(0,i+1);
                s2=word.substr(i+1);
                break;
            }
        }
        if(s1.empty()){
            return word;
        }
        for(int i=s1.size()-1;i>=0;i--){
            s.push_back(s1[i]);
        }
        return s+s2;
    }
};