"""Solution for Day 11 2025."""

import utils


def solve(data: list[str], part2=False):
    wiring = dict()
    for row in data:
        s, pair = row.split(": ")
        wiring[s] = pair.split(" ")

    memo = {}

    def count(curr, has_fft, has_dac):
        seen_fft = curr == "fft" or has_fft
        seen_dac = curr == "dac" or has_dac

        if part2 and curr == "out":
            return has_dac and has_fft
        elif not part2 and curr == "out":
            return 1

        key = (curr, has_fft, has_dac)
        if key in memo:
            return memo[key]

        total = 0
        for neighbour in wiring[curr]:
            total += count(neighbour, seen_fft, seen_dac)

        memo[key] = total
        return total

    return count("you", False, False) if not part2 else count("svr", False, False)


@utils.timer
def main(data):
    part_1 = solve(data)
    part_2 = solve(data, part2=True)

    return part_1, part_2
