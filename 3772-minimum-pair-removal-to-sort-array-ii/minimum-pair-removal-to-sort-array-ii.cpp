class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        vector<long long> a(nums.begin(), nums.end());
        vector<int> left(n), right(n);
        for (int i = 0; i < n; i++) {
            left[i] = i - 1;
            right[i] = (i + 1 < n ? i + 1 : -1);
        }
        using P = pair<long long, int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        for (int i = 0; i + 1 < n; i++) {
            pq.push({a[i] + a[i + 1], i});
        }

        // count inversions (bad positions)
        int bad = 0;
        for (int i = 0; i + 1 < n; i++) {
            if (a[i] > a[i + 1]) bad++;
        }

        int ops = 0;

        while (bad > 0) {
            auto [sum, i] = pq.top();
            pq.pop();

            int j = right[i];
            if (j == -1) continue;                
            if (left[j] != i) continue;           
            if (a[i] + a[j] != sum) continue;     
            int li = left[i];
            int rj = right[j];
            if (li != -1 && a[li] > a[i]) bad--;
            if (a[i] > a[j]) bad--;
            if (rj != -1 && a[j] > a[rj]) bad--;

            
            a[i] += a[j];

            // relink
            right[i] = rj;
            if (rj != -1) left[rj] = i;
            left[j] = right[j] = -1;

            // add new bad relations
            if (li != -1 && a[li] > a[i]) bad++;
            if (rj != -1 && a[i] > a[rj]) bad++;

            // push updated adjacent sums
            if (li != -1) pq.push({a[li] + a[i], li});
            if (rj != -1) pq.push({a[i] + a[rj], i});

            ops++;
        }

        return ops;
    }
};
