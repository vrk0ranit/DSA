class Solution {
public:
    static const long long INF = 4e18;

    unordered_map<string, vector<pair<string,long long>>> dp;
    unordered_map<string, unordered_map<string,long long>> dis;
    vector<long long> memo;

    void find(const string& node) {
        priority_queue<pair<long long,string>,
            vector<pair<long long,string>>,
            greater<pair<long long,string>>> pq;

        pq.push({0, node});
        dis[node][node] = 0;

        while (!pq.empty()) {
            auto [cost, u] = pq.top();
            pq.pop();

            if (dis[node][u] < cost) continue;

            for (auto &[v, w] : dp[u]) {
                if (!dis[node].count(v) || dis[node][v] > cost + w) {
                    dis[node][v] = cost + w;
                    pq.push({cost + w, v});
                }
            }
        }
    }

    long long dfs(string &s, string &t, int index, unordered_set<int>& lengths) {
        if (index == s.size()) return 0;
        if (memo[index] != -1) return memo[index];

        long long ans = INF;

        if (s[index] == t[index]) {
            ans = dfs(s, t, index + 1, lengths);
        }

        for (int len : lengths) {
            if (index + len > s.size()) continue;

            string u = s.substr(index, len);
            string v = t.substr(index, len);

            if (dis.count(u) && dis[u].count(v)) {
                ans = min(ans, dis[u][v] + dfs(s, t, index + len, lengths));
            }
        }

        return memo[index] = ans;
    }

    long long minimumCost(string source, string target,
                          vector<string>& original,
                          vector<string>& changed,
                          vector<int>& cost) {

        unordered_set<int> lengths;
        memo.assign(source.size(), -1);

        for (int i = 0; i < original.size(); i++) {
            dp[original[i]].push_back({changed[i], cost[i]});
            lengths.insert(original[i].size());
        }

        unordered_set<string> seen;
        for (auto &s : original) {
            if (!seen.count(s)) {
                find(s);
                seen.insert(s);
            }
        }

        long long res = dfs(source, target, 0, lengths);
        return res >= INF ? -1 : res;
    }
};
