use std::{
    fs::File,
    io::{BufReader, Read},
};

fn translate(c: char) -> i32 {
    if c == '(' {
        1
    } else if c == ')' {
        -1
    } else {
        0
    }
}

fn part_a(content: &str) -> i32 {
    content.chars().map(|c| translate(c)).sum()
}

fn part_b(content: &str) -> i32 {
    let mut acc = 0;

    for (i, c) in content.chars().enumerate() {
        acc += translate(c);
        if acc < 0 {
            return i as i32 + 1;
        }
    }

    -1
}

fn main() -> std::io::Result<()> {
    let file = File::open("b.in")?;
    let mut buf_reader = BufReader::new(file);
    let mut contents = String::new();
    buf_reader.read_to_string(&mut contents)?;

    let result_a = part_a(&contents);
    println!("part_a: {result_a}");
    let result_b = part_b(&contents);
    println!("part_b: {result_b}");

    Ok(())
}

#[test]
fn test_a() {
    assert_eq!(part_a("(())"), 0);
    assert_eq!(part_a("()()"), 0);
    assert_eq!(part_a("((("), 3);
    assert_eq!(part_a("(()(()("), 3);
    assert_eq!(part_a("))((((("), 3);
    assert_eq!(part_a("())"), -1);
    assert_eq!(part_a("))("), -1);
    assert_eq!(part_a(")))"), -3);
    assert_eq!(part_a(")())())"), -3);
}

#[test]
fn test_b() {
    assert_eq!(part_b(")"), 1);
    assert_eq!(part_b("()())"), 5);
}
