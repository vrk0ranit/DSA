class Solution {
public:
    bool isBalanced(string num) {
        int sumOdd=0;
        int sumEven=0;
        for(int i=0;i<num.size();i++){
            int digit=num[i]-'0';
            if(i%2==0){
                sumEven+=digit;
            }else{
                sumOdd+=digit;
            }
            
        }
        if(sumOdd==sumEven){
            return true;
        }else{
            return false;
        }
    }
};