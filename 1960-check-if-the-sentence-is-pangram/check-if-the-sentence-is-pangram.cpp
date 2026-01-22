class Solution {
public:
    bool checkIfPangram(string sentence) {
        vector<int> visibility(26,0);
        for(char ch : sentence){
            visibility[ch-'a']=1;
        }
        for(int i=0;i<26;i++){
            if(visibility[i]==0){
                return false;
            }
        }
        return true;
    }
};