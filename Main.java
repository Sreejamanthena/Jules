import java.util.*;

public class Main {
    private int V;
    private List<Integer>[] adj;
    private int time = 0;
    private int[] disc;
    private int[] low;
    private int[] parent;
    private Set<Integer> articulationPoints;

    public static void main(String[] args) {
        Main ppe = new Main();
        ppe.run();
    }

    void run() {
        Scanner sc = new Scanner(System.in);
        V = sc.nextInt();
        adj = new ArrayList[V];
        for (int i = 0; i < V; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (sc.nextInt() == 1) {
                    adj[i].add(j);
                }
            }
        }
        sc.close();

        findArticulationPoints();

        Set<Integer> typeBCities = new TreeSet<>();
        for (int ap : articulationPoints) {
            for (int neighbor : adj[ap]) {
                if (!articulationPoints.contains(neighbor)) {
                    typeBCities.add(neighbor);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int city : typeBCities) {
            sb.append(city).append(" ");
        }
        System.out.println(sb.toString().trim());
    }

    void findArticulationPoints() {
        disc = new int[V];
        low = new int[V];
        parent = new int[V];
        articulationPoints = new HashSet<>();
        boolean[] visited = new boolean[V];

        Arrays.fill(parent, -1);

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                dfs(i, visited);
            }
        }
    }

    void dfs(int u, boolean[] visited) {
        visited[u] = true;
        disc[u] = low[u] = ++time;
        int children = 0;

        for (int v : adj[u]) {
            if (!visited[v]) {
                children++;
                parent[v] = u;
                dfs(v, visited);

                low[u] = Math.min(low[u], low[v]);

                if (parent[u] == -1 && children > 1) {
                    articulationPoints.add(u);
                }

                if (parent[u] != -1 && low[v] >= disc[u]) {
                    articulationPoints.add(u);
                }
            } else if (v != parent[u]) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }
}
