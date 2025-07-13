#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

void dfs(int u, vector<bool>& visited, const vector<vector<int>>& adj) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v, visited, adj);
        }
    }
}

int count_connected_components(int n, const vector<vector<int>>& adj, int excluded_node = -1) {
    vector<bool> visited(n, false);
    int components = 0;
    for (int i = 0; i < n; ++i) {
        if (i == excluded_node) continue;
        if (!visited[i]) {
            dfs(i, visited, adj);
            components++;
        }
    }
    return components;
}

int main() {
    int n;
    cin >> n;

    vector<vector<int>> adj(n);
    vector<vector<int>> adj_matrix(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        string row_str;
        cin >> row_str;
        for (int j = 0; j < n; ++j) {
            adj_matrix[i][j] = row_str[j] - '0';
            if (adj_matrix[i][j] == 1) {
                adj[i].push_back(j);
            }
        }
    }

    int initial_components = count_connected_components(n, adj);

    vector<int> type_a_cities;
    for (int i = 0; i < n; ++i) {
        if (count_connected_components(n, adj, i) > initial_components) {
            type_a_cities.push_back(i);
        }
    }

    vector<int> type_b_cities;
    for (int city = 0; city < n; ++city) {
        bool is_type_b = false;
        bool is_type_a = false;
        for(int a_city : type_a_cities) {
            if(city == a_city) {
                is_type_a = true;
                break;
            }
        }
        if(is_type_a) continue;

        for (int a_city : type_a_cities) {
            if (adj_matrix[city][a_city] == 1) {
                is_type_b = true;
                break;
            }
        }
        if (is_type_b) {
            type_b_cities.push_back(city);
        }
    }

    sort(type_b_cities.begin(), type_b_cities.end());

    for (int i = 0; i < type_b_cities.size(); ++i) {
        cout << type_b_cities[i] << (i == type_b_cities.size() - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
