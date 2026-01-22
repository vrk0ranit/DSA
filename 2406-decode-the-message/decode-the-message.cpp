class Solution {
public:
    string decodeMessage(string key, string message) {
        vector<int> visited(26);
        vector<char> mapping(26,0);
        int curr='a';
        for(char ch : key){
            if(ch!=' ' && visited[ch-'a']==0){
                visited[ch-'a']=1;
                mapping[ch-'a']=curr;
                curr++;
            }
        }
        string result;
        for(char ch : message){
            if(ch==' '){
                result+=' ';
            }else{
                result+=mapping[ch-'a'];
            }
        }
        return result;
    }
};