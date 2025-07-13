import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char[][] grid = new char[n][n];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                grid[i][j] = line.charAt(j);
            }
        }
        String word = br.readLine();
        System.out.println(solve(grid, word));
    }

    private static int solve(char[][] grid, String word) {
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                count += search(grid, i, j, word);
            }
        }
        return count;
    }

    private static int search(char[][] grid, int r, int c, String word) {
        int count = 0;
        int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dc = {-1, 0, 1, -1, 1, -1, 0, 1};

        for (int i = 0; i < 8; i++) {
            if (searchDirection(grid, r, c, dr[i], dc[i], word)) {
                count++;
            }
        }
        return count;
    }

    private static boolean searchDirection(char[][] grid, int r, int c, int dr, int dc, String word) {
        int n = grid.length;
        for (int i = 0; i < word.length(); i++) {
            int newR = r + i * dr;
            int newC = c + i * dc;
            if (newR < 0 || newR >= n || newC < 0 || newC >= n || grid[newR][newC] != word.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}
