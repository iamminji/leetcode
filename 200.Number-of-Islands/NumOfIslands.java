/**
 * 200. Number of Islands
 * https://leetcode.com/problems/number-of-islands/description/
 */
public class NumOfIslands {
    public void dfs(int i, int j, char[][] grid, boolean[][] visited) {

        if (i + 1 < grid.length && !visited[i + 1][j] && grid[i + 1][j] == '1') {
            visited[i + 1][j] = true;
            dfs(i + 1, j, grid, visited);
        }
        if (j + 1 < grid[0].length && !visited[i][j + 1] && grid[i][j + 1] == '1') {
            visited[i][j + 1] = true;
            dfs(i, j + 1, grid, visited);
        }
        if (i - 1 >= 0 && !visited[i - 1][j] && grid[i - 1][j] == '1') {
            visited[i - 1][j] = true;
            dfs(i - 1, j, grid, visited);
        }
        if (j - 1 >= 0 && !visited[i][j - 1] && grid[i][j - 1] == '1') {
            visited[i][j - 1] = true;
            dfs(i, j - 1, grid, visited);
        }
    }

    public int numIslands(char[][] grid) {

        if (grid.length == 0) {
            return 0;
        }
        int N = grid.length;
        int M = grid[0].length;
        boolean[][] visited = new boolean[N][M];
        int cnt = 0;
        for (int j = 0; j < M; ++j) {
            for (int i = 0; i < N; ++i) {
                if (!visited[i][j] && grid[i][j] == '1') {
                    visited[i][j] = true;
                    dfs(i, j, grid, visited);
                    cnt += 1;
                }
            }
        }
        return cnt;
    }
}
