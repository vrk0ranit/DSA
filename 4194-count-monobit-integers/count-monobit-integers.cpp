class Solution {
public:
    int countMonobit(int n) {
        int count = 1; // 0 is always monobit
        int val = 1;   // starts with 2^1 - 1 = 1
        while (val <= n) {
            count++;
            val = (val << 1) | 1;  // generate next monobit number
        }
        return count;
    }
};