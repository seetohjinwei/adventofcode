import java.io.*;
import java.util.*;

public class day6 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("a.in");
        Scanner sc = new Scanner(file);
        String[] input = sc.next().split(",");
        sc.close();

        long[] fishes = new long[9];
        for (String in : input) {
            int value = Integer.parseInt(in);
            fishes[value]++;
        }

        // just change days for different part
        int days = 256;
        while (days-- > 0) {
            long toReproduce = fishes[0];
            for (int i = 0; i < 8; i++) {
                fishes[i] = fishes[i+1];
            }
            fishes[6] += toReproduce;
            fishes[8] = toReproduce;
        }

        long totalFish = 0;
        for (long fish : fishes) {
            totalFish += fish;
        }

        System.out.println(totalFish);
        return;
    }
}
