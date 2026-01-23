class Solution {
public:
    bool hasSameDigits(string s) {
        while (s.size() > 2) {
            string sum;
            for (int i = 0; i < s.size() - 1; i++) {
                int rem = (s[i] - '0' + s[i + 1] - '0') % 10;
                sum.push_back(rem + '0');
            }
            s = sum; 
        }
        return s[0] == s[1];
    }
};
