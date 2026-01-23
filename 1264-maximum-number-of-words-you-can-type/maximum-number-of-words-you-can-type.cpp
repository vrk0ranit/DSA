class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        int count=0;
        vector<bool> broken(26,false);
        for(char c : brokenLetters){
            broken[c-'a']=true;
        }

        stringstream ss(text);
        string word;
        vector<string> words;
        while(ss >> word){
            bool canType=true;
            for(char w: word){
                if(broken[w-'a']){
                    canType=false;
                    break;
                }
            }
            if(canType){
                count++;
            }
        }
        return count;    
    }
};
