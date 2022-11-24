import java.io.*;
import java.util.*;

class Point {
    public int x;
    public int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return String.format("%d,%d", this.x, this.y);
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        } else if (other instanceof Point) {
            Point otherPoint = (Point) other;
            return this.x == otherPoint.x && this.y == otherPoint.y;
        } else {
            return false;
        }
    }
}

class Vent {
    private Point A;
    private Point B;

    public Vent(int x1, int y1, int x2, int y2) {
        this.A = new Point(x1, y1);
        this.B = new Point(x2, y2);
    }

    public boolean isHorizontalOrVertical() {
        return this.A.x == this.B.x
            || this.A.y == this.B.y;
    }

    public boolean isDiagonal() {
        return Math.abs(this.A.x - this.B.x)
            == Math.abs(this.A.y - this.B.y);
    }

    public List<Point> allPoints() {
        List<Point> points = new ArrayList<>();

        if (isHorizontalOrVertical()) {
            int startX = Math.min(this.A.x, this.B.x);
            int endX = Math.max(this.A.x, this.B.x);
            int startY = Math.min(this.A.y, this.B.y);
            int endY = Math.max(this.A.y, this.B.y);
            for (int x = startX; x <= endX; x++) {
                for (int y = startY; y <= endY; y++) {
                    Point point = new Point(x, y);
                    points.add(point);
                }
            }
        } else if (isDiagonal()) {
            Point a = this.A.x < this.B.x ? A : B;
            Point b = this.A.x < this.B.x ? B : A;
            int difference = b.x - a.x;
            int modifier = (a.y < b.y) ? 1 : -1;
            // modifier depends on if / or \
            // the diagonal's shape
            for (int d = 0; d <= difference; d++) {
                int x = a.x + d;
                int y = a.y + (modifier * d);
                Point point = new Point(x, y);
                points.add(point);
            }
        }
        // if not horizontal nor vertical nor diagonal, do nothing
        return points;
    }

    @Override
    public String toString() {
        return String.format("A: %s, B: %s", this.A, this.B);
    }
}

class day5 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("a.in");
        Scanner sc = new Scanner(file);
        
        List<Vent> vents = new ArrayList<>();
        while (sc.hasNextLine()) {
            String[] input = sc.nextLine().split("(,| -> )");
            vents.add(new Vent(
                Integer.parseInt(input[0]),
                Integer.parseInt(input[1]),
                Integer.parseInt(input[2]),
                Integer.parseInt(input[3])
            ));
        }

        Map<String, Integer> part1 = new HashMap<>();
        Map<String, Integer> part2 = new HashMap<>();

        for (Vent vent : vents) {
            List<Point> points = vent.allPoints();
            for (Point point : points) {
                String pointAsString = point.toString();
                if (vent.isHorizontalOrVertical()) {
                    part1.put(
                        pointAsString,
                        part1.getOrDefault(pointAsString, 0) + 1
                    );
                }
                part2.put(
                        pointAsString,
                        part2.getOrDefault(pointAsString, 0) + 1
                    );
            }
        }

        int result1 = 0;
        for (int x : part1.values()) {
            if (x > 1) result1++;
        }
        System.out.println(result1);

        int result2 = 0;
        for (int x : part2.values()) {
            if (x > 1) result2++;
        }
        System.out.println(result2);

        sc.close();
        return;
    }
}
