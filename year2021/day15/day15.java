import java.io.*;
import java.util.*;

public class day15 {
    public static void main(String[] args) throws FileNotFoundException {
        // parsing input
        File file = new File("a.in");
        Scanner sc = new Scanner(file);
        List<String> lines = new ArrayList<>();
        while (sc.hasNextLine()) {
            lines.add(sc.nextLine());
        }
        sc.close();

        // initialising primitive 2d input array
        int row = lines.size();
        int col = lines.get(0).length();
        int[][] input = new int[row][col];
        for (int i = 0; i < row; i++) {
            String line = lines.get(i);
            for (int j = 0; j < col; j++) {
                input[i][j] = line.charAt(j) - '0'; 
            }
        }

        // part 1
        int[][] dp1 = new int[row][col];
        for (int r = row - 1; r >= 0; r--) {
            for (int c = col - 1; c >= 0; c--) {
                if (r == row - 1 && c == col - 1) {
                    // bottom right cell
                    dp1[r][c] = input[r][c];
                } else {
                    // not sure if part 1 was a fluke of not needing top and left (but gave me correct answer)
                    int bottom = (r + 1 == row) ? Integer.MAX_VALUE : dp1[r + 1][c];
                    int right = (c + 1 == col) ? Integer.MAX_VALUE : dp1[r][c + 1];
                    dp1[r][c] = input[r][c] + Math.min(bottom, right); 
                }
            }
        }
        System.out.println("Part 1: " + (dp1[0][0] - input[0][0]));

        // part 2
        int nrow = row * 5;
        int ncol = col * 5;
        int[][] dp2 = new int[nrow][ncol];
        boolean changed = false;
        // int iter = 0; // check how many loops this takes for fun
        do {
            // iter++;
            changed = false;
            for (int r = nrow - 1; r >= 0; r--) {
                for (int c = ncol - 1; c >= 0; c--) {
                    int val = input[r % row][c % col];
                    int mod = r / row + c / col;
                    int nval = (val + mod - 1) % 9 + 1;
                    if (r == nrow - 1 && c == ncol - 1) {
                        // bottom right cell
                        dp2[r][c] = nval;
                    } else {
                        int og = dp2[r][c];
                        // if 0 then ignore (definitely not saved before), saves A LOT of iterations (1000+ vs 44)
                        int top = (r == 0 || dp2[r - 1][c] == 0) ? Integer.MAX_VALUE : dp2[r - 1][c];
                        int left = (c == 0  || dp2[r][c - 1] == 0) ? Integer.MAX_VALUE : dp2[r][c - 1];
                        int bottom = (r + 1 == nrow || dp2[r + 1][c] == 0) ? Integer.MAX_VALUE : dp2[r + 1][c];
                        int right = (c + 1 == ncol  || dp2[r][c + 1] == 0) ? Integer.MAX_VALUE : dp2[r][c + 1];
                        dp2[r][c] = nval + Math.min(Math.min(top, left), Math.min(bottom, right));
                        if (dp2[r][c] != og) {
                            changed = true;
                        }
                    }
                }
            }
        } while (changed);
        System.out.println("Part 2: " + (dp2[0][0] - input[0][0]));
        // took 44 iterations of the do-while loop (for my a.in)
        // System.out.println(iter);
    }
}
