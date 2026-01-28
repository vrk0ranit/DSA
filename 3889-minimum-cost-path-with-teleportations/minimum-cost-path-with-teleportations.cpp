class Solution {
public:
    static const int M = 10001;   // max grid value
    static const int NN = 6400;   // 80 * 80
    static const int INF = 1e9;

    // value -> positions
    vector<int> x_pos[M];
    unsigned dp[11][NN];
    unsigned suffixMin[M];

    static inline int idx(int i, int j, int c) {
        return i * c + j;
    }

    int minCost(vector<vector<int>>& grid, int k) {
        int r = grid.size(), c = grid[0].size();
        int N = r * c;
        int xMax = 0;

        // group positions by grid value
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                int x = grid[i][j];
                x_pos[x].push_back(idx(i, j, c));
                xMax = max(xMax, x);
            }
        }

        // init dp
        for (int t = 0; t <= k; t++)
            fill(dp[t], dp[t] + N, INF);

        // base case: 0 teleport
        dp[0][0] = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                int pos = idx(i, j, c);
                int x = grid[i][j];
                if (i > 0)
                    dp[0][pos] = min(dp[0][pos],
                                     dp[0][idx(i - 1, j, c)] + x);
                if (j > 0)
                    dp[0][pos] = min(dp[0][pos],
                                     dp[0][idx(i, j - 1, c)] + x);
            }
        }

        // dp with teleports
        for (int t = 1; t <= k; t++) {
            // build suffix minimum
            unsigned currMin = INF;
            for (int x = xMax; x >= 0; x--) {
                for (int p : x_pos[x])
                    currMin = min(currMin, dp[t - 1][p]);
                suffixMin[x] = currMin;
            }

            // transition
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    int pos = idx(i, j, c);
                    int x = grid[i][j];

                    // no teleport or teleport
                    dp[t][pos] = min(dp[t - 1][pos], suffixMin[x]);

                    // normal moves
                    if (i > 0)
                        dp[t][pos] = min(dp[t][pos],
                                         dp[t][idx(i - 1, j, c)] + x);
                    if (j > 0)
                        dp[t][pos] = min(dp[t][pos],
                                         dp[t][idx(i, j - 1, c)] + x);
                }
            }
        }

        int ans = dp[k][N - 1];

        // cleanup
        for (int x = 0; x <= xMax; x++)
            x_pos[x].clear();

        return ans;
    }
};
