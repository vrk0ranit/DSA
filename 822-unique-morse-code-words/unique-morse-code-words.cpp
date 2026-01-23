class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector<string> morseCode={".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        unordered_set<string> s;
        for(auto &word : words){
            string t;
            for(char &ch : word){
                t+=morseCode[ch-'a'];
            }
            s.insert(t);
        }
        return s.size();
    }
};