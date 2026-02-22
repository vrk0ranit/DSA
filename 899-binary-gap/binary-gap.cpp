class Solution {
public:
    int binaryGap(int n) {
        int last = -1;   // last position of 1
        int maxDist = 0;
        int pos = 0;

        while (n > 0) {

            if (n & 1) {   // if last bit is 1

                if (last != -1) {
                    maxDist = max(maxDist, pos - last);
                }

                last = pos;
            }

            n = n >> 1;  // right shift
            pos++;
        }

        return maxDist;
    }
};