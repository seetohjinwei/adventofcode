use std::fs;

fn part_a(content: &str) -> i32 {
    content
        .split("\n")
        .map(|line| {
            let v: Vec<i32> = line.split("x").map(|c| c.parse().unwrap()).collect();
            let (l, w, h) = (v[0], v[1], v[2]);

            let a = l * w;
            let b = w * h;
            let c = h * l;

            let extra = i32::min(a, i32::min(b, c));
            2 * (a + b + c) + extra
        })
        .sum()
}

fn part_b(content: &str) -> i32 {
    content
        .split("\n")
        .map(|line| {
            let v: Vec<i32> = line.split("x").map(|c| c.parse().unwrap()).collect();
            let (l, w, h) = (v[0], v[1], v[2]);

            let a = l + l + w + w;
            let b = w + w + h + h;
            let c = h + h + l + l;

            let wrap = i32::min(a, i32::min(b, c));
            wrap + l * w * h
        })
        .sum()
}

fn main() {
    let contents = fs::read_to_string("b.in").expect("File is missing");
    println!("part_a: {}", part_a(&contents));
    println!("part_b: {}", part_b(&contents));
}
