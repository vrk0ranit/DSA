class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        int n=words.size();
        int count=0;
        vector<string> reversed(n);
        for(int i=0;i<n;i++){
            reversed[i]=words[i];
            reverse(reversed[i].begin(),reversed[i].end());
        }
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(words[i]==reversed[j]){
                    count++;
                }
            }
        }
        return count;
    }
};