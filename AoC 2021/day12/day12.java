import java.io.*;
import java.util.*;

class Node {
    public String name;
    public Set<String> links;
    public boolean isSmall;

    private boolean isLowerCase(String s) {
        return Character.isLowerCase(s.charAt(0));
    }

    public Node(String name) {
        this.name = name;
        this.links = new HashSet<>();
        this.isSmall = isLowerCase(name);
    }
}

class Solution {
    private Map<String, Node> NodeMap;
    
    public int pathFindPartOne(String name, Set<String> smallVisited) {
        Node node = this.NodeMap.get(name);
        Set<String> smallVisitedCopy = new HashSet<>(smallVisited);
        if (name.equals("end")) {
            return 1;
        } else if (node.isSmall) {
            if (smallVisitedCopy.contains(name)) {
                return 0;
            } else {
                smallVisitedCopy.add(name);
            }
        }
        int result = 0;
        Set<String> nexts = new HashSet<>(node.links);
        for (String next : nexts) {
            result += pathFindPartOne(next, smallVisitedCopy);
        }
        return result;
    }
    
    public int pathFindPartTwo(String name, Set<String> smallVisited, boolean visitTwice) {
        Node node = this.NodeMap.get(name);
        Set<String> smallVisitedCopy = new HashSet<>(smallVisited);
        if (name.equals("end")) {
            return 1;
        } else if (node.isSmall) {
            if (smallVisitedCopy.contains(name)) {
                if (name.equals("start") || visitTwice) {
                    return 0;
                } else {
                    visitTwice = true;
                }
            } else {
                smallVisitedCopy.add(name);
            }
        }
        int result = 0;
        Set<String> nexts = new HashSet<>(node.links);
        for (String next : nexts) {
            result += pathFindPartTwo(next, smallVisitedCopy, visitTwice);
        }
        return result; 
    }

    Solution() throws FileNotFoundException {
        File file = new File("a.in");
        Scanner sc = new Scanner(file);
        this.NodeMap = new HashMap<>();
        while (sc.hasNextLine()) {
            String[] line = sc.nextLine().split("-");
            Node node0 = this.NodeMap.getOrDefault(line[0], new Node(line[0]));
            node0.links.add(line[1]);
            this.NodeMap.put(line[0], node0);
            Node node1 = this.NodeMap.getOrDefault(line[1], new Node(line[1]));
            node1.links.add(line[0]);
            this.NodeMap.put(line[1], node1);
        }
        sc.close();
    }
}

public class day12 {
    public static void main(String[] args) throws FileNotFoundException {
        Solution solution = new Solution();
        System.out.println("Part 1: " + solution.pathFindPartOne("start", new HashSet<>()));
        System.out.println("Part 2: " + solution.pathFindPartTwo("start", new HashSet<>(), false));
    }
}
