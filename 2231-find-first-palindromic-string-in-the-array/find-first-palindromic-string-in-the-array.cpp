class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        string pal="";
        for(auto &word : words){
            for(int i=word.size()-1;i>=0;i--){
                pal+=word[i];
            }
            if(pal==word){
                break;
            }else{
                pal="";
            }         
        }
        return pal;
    }
};