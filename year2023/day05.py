with open("day05.in") as f:
    data = f.read().strip()


def parse_input(data: str):
    initial_seeds, *maps = data.split("\n\n")
    initial_seeds = [int(x) for x in initial_seeds.split(": ", 1)[1].split(" ")]
    maps = [
        [
            tuple(int(x) for x in row.split(" "))
            for i, row in enumerate(m.split("\n"))
            if i != 0
        ] for m in maps
    ]

    return initial_seeds, maps


def get_part1(data: str) -> int:
    initial_seeds, maps = parse_input(data)

    def get_location(seed: int) -> int:
        result = seed

        for map_ in maps:
            for (b, a, length) in map_:
                dist = result - a
                if dist >= 0 and dist < length:
                    result = b + dist
                    break

        return result

    return min(get_location(seed) for seed in initial_seeds)


def get_part2(data: str) -> int:
    seeds, maps = parse_input(data)

    chunks = [[seeds[i], seeds[i] + seeds[i+1] - 1] for i in range(0, len(seeds), 2)]
    chunks.sort(key=lambda x: x[0])

    for map_ in maps:
        map_.sort(key=lambda x: x[1])
        new_chunks = []
        chunk_index = 0

        for (b, a, length) in map_:
            lo = a
            hi = b + length - 1
            if chunk_index >= len(chunks):
                break
            chunk_lo, chunk_hi = chunks[chunk_index]
            if chunk_lo < lo:
                new_chunks.append((chunk_lo, lo - 1))

        print(chunks)
        print(map_)

        chunks = new_chunks

    def get_location(seed: int, range: int) -> int:
        result = seed

        for map_ in maps:
            for (b, a, length) in map_:
                dist = result - a
                if dist >= 0 and dist < length:
                    result = b + dist
                    break

        return result

    return min(get_location(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2))


part1 = get_part1(data)
part2 = get_part2(data)

print(f"part1: {part1}")
print(f"part2: {part2}")
