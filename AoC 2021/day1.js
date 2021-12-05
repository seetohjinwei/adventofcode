// Source Academy

// part 2

const input = prompt("input");
// need to paste the input into the prompt window

const L = array_length(input);
let current = "";
const arr = [];

for (let i = 0; i < L; i = i + 1) {
    const char = char_at(input, i);
    if (char === "\n") {
        arr[array_length(arr)] = parse_int(current, 10);
        current = "";
    } else {
        current = current + char;
    }
}
arr[array_length(arr)] = parse_int(current, 10);
// now arr is ready

let result = 0;
let prev_window = arr[0] + arr[1] + arr[2];

for (let i = 3; i < array_length(arr); i = i + 1) {
    const new_window = prev_window - arr[i - 3] + arr[i];
    if (new_window > prev_window) {
        result = result + 1;
    }
    prev_window = new_window;
}

display(result);
