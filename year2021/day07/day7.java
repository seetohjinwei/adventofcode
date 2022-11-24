import java.io.*;
import java.util.*;

public class day7 {
    private static int part1(int[] crabs) {
        int sum = 0;
        for (int pos : crabs) {
            sum += pos;
        }
        int N = crabs.length;
        int prevFuel = sum - (N - 1) * crabs[0];
        int lowestFuel = prevFuel;
        for (int i = 1; i < N; i++) {
            int sizePrev = i;
            int sizeNext = N - i;
            int diff = crabs[i] - crabs[i - 1];
            int currentFuel = prevFuel + diff * sizePrev - diff * sizeNext;
            if (currentFuel < lowestFuel) {
                lowestFuel = currentFuel;
            }
            prevFuel = currentFuel;
        }
        return lowestFuel;
    }

    private static int triangleNumber(int n) {
        return (n * (n + 1)) / 2;
    }

    private static int part2(int[] crabs) {
        int N = crabs.length;
        int lowestFuel = Integer.MAX_VALUE;
        for (int n = 0; n < crabs[N - 1]; n++) {
            int currentFuel = 0;
            for (int i = 0; i < N; i++) {
                currentFuel += triangleNumber(Math.abs(crabs[i] - n));
            }
            if (currentFuel < lowestFuel) {
                lowestFuel = currentFuel;
            }
        }
        return lowestFuel;
    }

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("a.in");
        Scanner sc = new Scanner(file);
        int[] crabs = Arrays.stream(sc.next().split(","))
                            .mapToInt(Integer::valueOf)
                            .toArray();
        sc.close();
        Arrays.sort(crabs);

        System.out.println(part1(crabs));
        System.out.println(part2(crabs));
        return;
    }
}
