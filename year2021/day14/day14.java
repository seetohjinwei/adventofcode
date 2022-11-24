import java.io.*;
import java.util.*;

class Pair {
    public String first;
    public String second;

    public Pair(String first, String second) {
        this.first = first;
        this.second = second;
    }
}

public class day14 {
    public static long solve(int steps) throws FileNotFoundException {
        File file = new File("a.in");
        Scanner sc = new Scanner(file);
        String inputString = sc.nextLine();
        Map<String, Long> counter = new HashMap<>();
        for (int i = 0; i < inputString.length() - 1; i++) {
            String s = "" + inputString.charAt(i) + inputString.charAt(i + 1);
            counter.put(s, counter.getOrDefault(s, 0L) + 1);
        }
        Map<String, Pair> map = new HashMap<>();
        sc.nextLine();
        while (sc.hasNextLine()) {
            String[] line = sc.nextLine().split(" -> ");
            String from = line[0];
            String to = line[1];
            String left = from.substring(0, 1) + to;
            String right = to + from.substring(1);
            Pair p = new Pair(left, right);
            map.put(from, p);
        }
        sc.close(); 
        
        for (int i = 0; i < steps; i++) {
            Map<String, Long> counterCopy = new HashMap<>();
            for (String s : counter.keySet()) {
                long count = counter.get(s);
                if (map.containsKey(s)) {
                    Pair p = map.get(s);
                    counterCopy.put(p.first, counterCopy.getOrDefault(p.first, 0L) + count);
                    counterCopy.put(p.second, counterCopy.getOrDefault(p.second, 0L) + count);
                } else {
                    counterCopy.put(s, counterCopy.getOrDefault(s, 0L) + count);
                }
            }
            counter = new HashMap<>(counterCopy);
        }
        Map<Character, Long> charCounter = new HashMap<>();
        for (String s : counter.keySet()) {
            long count = counter.get(s);
            char first = s.charAt(0);
            char second = s.charAt(1);
            charCounter.put(first, charCounter.getOrDefault(first, 0L) + count);
            charCounter.put(second, charCounter.getOrDefault(second, 0L) + count);
        }
        long minQuantity = Long.MAX_VALUE;
        long maxQuantity = Long.MIN_VALUE;
        for (char c : charCounter.keySet()) {
            long count = charCounter.get(c);
            char firstCharInput = inputString.charAt(0);
            char lastCharInput = inputString.charAt(inputString.length() - 1);
            if (c == firstCharInput) count++;
            if (c == lastCharInput) count++;
            long actual = count / 2;
            minQuantity = Math.min(actual, minQuantity);
            maxQuantity = Math.max(actual, maxQuantity);
        }
        // System.out.println(maxQuantity + " " + minQuantity);
        return maxQuantity - minQuantity;
    }
    public static void main(String[] args) throws FileNotFoundException {
        System.out.println("Part 1: " + solve(10));
        System.out.println("Part 2: " + solve(40));
    }
}
