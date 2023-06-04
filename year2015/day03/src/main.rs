use std::{collections::HashSet, fs};

#[derive(Hash, Eq, PartialEq, Copy, Clone)]
struct Location(i32, i32);

impl Location {
    fn translate(c: char) -> Self {
        if c == '^' {
            Location(0, -1)
        } else if c == 'v' {
            Location(0, 1)
        } else if c == '<' {
            Location(-1, 0)
        } else if c == '>' {
            Location(1, 0)
        } else {
            panic!("Unknown character: {}", c);
        }
    }

    fn next_location(&self, c: char) -> Self {
        let other = Location::translate(c);
        Location(self.0 + other.0, self.1 + other.1)
    }
}

fn part_a(contents: &str) -> usize {
    let mut seen = HashSet::new();
    let mut curr: Location = Location(0, 0);
    seen.insert(curr);

    for c in contents.chars() {
        curr = curr.next_location(c);
        seen.insert(curr);
    }

    seen.len()
}

fn part_b(contents: &str) -> usize {
    let mut seen = HashSet::new();
    let mut santa: Location = Location(0, 0);
    let mut robot: Location = Location(0, 0);
    seen.insert(santa);

    for (i, c) in contents.chars().enumerate() {
        if i % 2 == 0 {
            santa = santa.next_location(c);
            seen.insert(santa);
        } else {
            robot = robot.next_location(c);
            seen.insert(robot);
        }
    }

    seen.len()
}

fn main() {
    let contents = fs::read_to_string("b.in").expect("File is missing");
    println!("part_a: {}", part_a(&contents));
    println!("part_b: {}", part_b(&contents));
}
