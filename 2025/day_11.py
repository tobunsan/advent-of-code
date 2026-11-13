"""Solution for Day 11 2025."""

import utils


def solve(data: list[str], part2=False):
    wiring = dict()
    for row in data:
        s, pair = row.split(": ")
        wiring[s] = pair.split(" ")

    memo = {}

    def count(curr):
        if curr == "out":
            return 1

        if curr in memo:
            return memo[curr]

        total = 0
        for neighbour in wiring[curr]:
            total += count(neighbour)

        memo[curr] = total
        return total

    return count("you")


def solve2(data: list[str]):
    wiring = dict()
    for row in data:
        s, pair = row.split(": ")
        wiring[s] = pair.split(" ")

    memo = {}

    def count(curr, has_fft, has_dac):
        seen_fft = curr == "fft" or has_fft
        seen_dac = curr == "dac" or has_dac
        if curr == "out":
            if has_dac and has_fft:
                return 1
            else:
                return 0

        key = (curr, has_fft, has_dac)
        if key in memo:
            return memo[key]

        total = 0
        for neighbour in wiring[curr]:
            total += count(neighbour, seen_fft, seen_dac)

        memo[key] = total
        return total

    return count("svr", False, False)


@utils.timer
def main(data):
    part_1 = solve(data)
    part_2 = solve2(data)

    return part_1, part_2
