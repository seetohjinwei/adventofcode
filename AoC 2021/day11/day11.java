import java.io.*;
import java.util.*;

class Solution {
    private int[][] octopuses;
    private boolean[][] flashed;
    private int steps;
    public int flashes;
    public int firstFlash;

    Solution(int[][] octopuses) {
        this.octopuses = octopuses;
        this.flashed = new boolean[10][10];
        this.steps = 0;
        this.flashes = 0;
        this.firstFlash = -1;
    }
    
    void run() {
        while (this.steps++ < 100 || this.firstFlash == -1) {
            // tick each octopus
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    tick(i, j);
                }
            }
            // setting to 0
            int numberOfFlashes = 0;
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    if (this.flashed[i][j]) {
                        numberOfFlashes++;
                        this.octopuses[i][j] = 0;
                        this.flashed[i][j] = false;
                    }
                }
            }
            if (numberOfFlashes == 100 && this.firstFlash == -1) {
                this.firstFlash = steps;
            }
        }
    }
    
    void tick(int r, int c) {
        if (r < 0 || r > 9 || c < 0 || c > 9) {
            return;
        }
        this.octopuses[r][c]++;
        if (this.flashed[r][c] || this.octopuses[r][c] <= 9) {
            return;
        }
        if (this.steps <= 100) {
            // part 1 ends at step 100
            this.flashes++;
        }
        this.flashed[r][c] = true;
        tick(r - 1, c - 1);
        tick(r - 1, c);
        tick(r - 1, c + 1);
        tick(r, c - 1);
        tick(r, c + 1);
        tick(r + 1, c - 1);
        tick(r + 1, c);
        tick(r + 1, c + 1);
    }
}

public class day11 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("a.in");
        Scanner sc = new Scanner(file);
        int[][] octopuses = new int[10][10];
        for (int i = 0; i < 10; i ++) {
            String[] line = sc.nextLine().split("");
            for (int j = 0; j < 10; j++) {
                octopuses[i][j] = line[j].charAt(0) - '0';
            }
        }
        Solution solution = new Solution(octopuses);
        solution.run();
        System.out.println(solution.flashes);
        System.out.println(solution.firstFlash);
        sc.close();
    }
}
