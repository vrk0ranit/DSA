class Solution {
public:
    int compress(vector<char>& chars) {
        int n=chars.size();
        int i=0;
        int idx=0;
        while(i<n){
            int current=chars[i];
            int count=0;
            while(i<n && current==chars[i]){
                count++;
                i++;
            }
            chars[idx++]=current;
            if(count>1){
                string ct=to_string(count);
                for(char c : ct){
                    chars[idx++]=c;
                }
            }
        }
        return idx;
    }
};