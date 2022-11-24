import java.io.*;
import java.util.*;

class Solution1 {
    private String initialInput;
    private Map<String, Character> map;

    public int PartOne() {
        List<Character> list = new ArrayList<Character>();
        for (char c : this.initialInput.toCharArray()) {
            list.add(c);
        }
        final int totalSteps = 10;
        for (int steps = 0; steps < totalSteps; steps++) {
            for (int i = 0; i < list.size() - 1; i++) {
                char current = list.get(i);
                char next = list.get(i + 1);
                String s = "" + current + next;
                if (this.map.containsKey(s)) {
                    char toInsert = this.map.get(s);
                    list.add(i + 1, toInsert);
                    i++;
                }
            }
        }
        Map<Character, Integer> counter = new HashMap<>();
        for (char c : list) {
            counter.put(c, counter.getOrDefault(c, 0) + 1);
        }
        int maxQuantity = Integer.MIN_VALUE;
        int minQuantity = Integer.MAX_VALUE;
        for (int q : counter.values()) {
            maxQuantity = Math.max(q, maxQuantity);
            minQuantity = Math.min(q, minQuantity);
        }
        // System.out.println(maxQuantity + " " + minQuantity);
        return maxQuantity - minQuantity;
    }

    public Solution1() throws FileNotFoundException {
        File file = new File("a.in");
        Scanner sc = new Scanner(file);
        this.initialInput = sc.nextLine();
        this.map = new HashMap<String, Character>();
        sc.nextLine();
        while (sc.hasNextLine()) {
            String[] line = sc.nextLine().split(" -> ");
            this.map.put(line[0], line[1].charAt(0));
        }
        sc.close();
    }
}

public class day14naive {
    public static void main(String[] args) throws FileNotFoundException {
        Solution1 solution = new Solution1();
        System.out.println("Part 1: " + solution.PartOne());
    }
}
