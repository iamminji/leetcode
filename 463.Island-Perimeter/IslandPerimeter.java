
/**
 * 463. Island Perimeter
 * https://leetcode.com/problems/island-perimeter/description/
 */

public class IslandPerimeter {

    public int dfs(int i, int j, int[][] grid, boolean[][] visited) {

        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] == 0) {
            return 1;
        }
        if (visited[i][j]) {
            return 0;
        }
        visited[i][j] = true;

        int res = 0;

        res += dfs(i - 1, j, grid, visited);
        res += dfs(i, j - 1, grid, visited);
        res += dfs(i + 1, j, grid, visited);
        res += dfs(i, j + 1, grid, visited);

        return res;
    }

    public int islandPerimeter(int[][] grid) {

        if (grid == null || grid.length == 0) {
            return 0;
        }
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int result = 0;
        for (int i = 0; i < grid.length; ++i) {
            for (int j = 0; j < grid[i].length; ++j) {
                if (!visited[i][j] && grid[i][j] == 1) {
                    result += dfs(i, j, grid, visited);
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        IslandPerimeter main = new IslandPerimeter();
        int[][] grid = {{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {1, 1, 0, 0}};
        System.out.println(main.islandPerimeter(grid));
    }
}
