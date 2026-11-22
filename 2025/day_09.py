"""Solution for Day 9 2025."""

from itertools import combinations

import utils


def compress_matrix(data):
    matrix = [list(map(int, c.split(","))) for c in data]
    col_list = sorted(set([c for c, _ in matrix]))
    row_list = sorted(set([r for _, r in matrix]))

    def _create_compressed_row(coord_list):
        start = 1
        compress = {coord_list[0]: start}
        prev = coord_list[0]
        for i in range(1, len(coord_list)):
            curr = coord_list[i]

            if curr - prev > 1:
                start += 1
                compress[prev + 1] = start

            start += 1
            compress[curr] = start
            prev = curr

        return compress

    compressed_col = _create_compressed_row(col_list)
    compressed_row = _create_compressed_row(row_list)

    compressed_hash = {}
    compressed_matrix = []
    for p in matrix:
        c, r = p
        compressed_matrix.append([compressed_col[c], compressed_row[r]])
        compressed_hash[tuple(p)] = (compressed_col[c], compressed_row[r])

    max_c = max(c for c, _ in compressed_matrix)
    max_r = max(r for _, r in compressed_matrix)

    compressed_grid = [["." for _ in range(max_c + 2)] for _ in range(max_r + 2)]

    prev = compressed_matrix[-1]

    for c, r in compressed_matrix:
        prev_c, prev_r = prev

        if prev_c == c:
            for i in range(min(r, prev_r), max(r, prev_r) + 1):
                compressed_grid[i][c] = "#"

        elif prev_r == r:
            for i in range(min(c, prev_c), max(c, prev_c) + 1):
                compressed_grid[r][i] = "#"

        prev = c, r

    outer_border = flood_fill_outer(compressed_grid)
    return compressed_hash, outer_border


def flood_fill_outer(matrix):
    stack = [(0, 0)]
    outer_border = set()
    while stack:
        r, c = stack.pop()

        if (r, c) in outer_border:
            continue

        outer_border.add((r, c))
        for dr in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr[0], c + dr[1]

            if (
                nc < 0
                or nc >= len(matrix[0])
                or nr < 0
                or nr >= len(matrix)
                or matrix[nr][nc] == "#"
            ):
                continue
            stack.append((nr, nc))
    return outer_border


def check_validity_for(point1, point2, outer_border):

    c1, r1 = point1
    c2, r2 = point2
    min_c = min(c1, c2)
    max_c = max(c1, c2)
    min_r = min(r1, r2)
    max_r = max(r1, r2)

    p1, p2, p3, p4 = (min_c, min_r), (max_c, min_r), (max_c, max_r), (min_c, max_r)

    prev = p4

    for c, r in (p1, p2, p3, p4):
        prev_c, prev_r = prev

        if prev_c == c:
            for i in range(min(r, prev_r), max(r, prev_r) + 1):
                if (i, c) in outer_border:
                    return False

        elif prev_r == r:
            for i in range(min(c, prev_c), max(c, prev_c) + 1):
                if (r, i) in outer_border:
                    return False
        prev = c, r

    return True


def solve(data, part2=False):
    coords = [list(map(int, c.split(","))) for c in data]
    result = 0
    compressed_hash, outer_border = compress_matrix(data)

    for (x1, y1), (x2, y2) in combinations(coords, 2):

        x_area = abs(x1 - x2) + 1
        y_area = abs(y1 - y2) + 1
        curr_area = x_area * y_area
        if curr_area < result:
            continue
        if part2 and (
            not check_validity_for(
                compressed_hash[(x1, y1)], compressed_hash[(x2, y2)], outer_border
            )
        ):
            continue
        result = curr_area

    return result


@utils.timer
def main(data):

    part_1 = solve(data)
    part_2 = solve(data, True)

    return part_1, part_2


if __name__ == "__main__":

    data = utils.get_data(9)
    part_1, part_2 = main(data)

    utils.print_solution(2025, 9, "Part 1", part_1)
    utils.print_solution(2025, 9, "Part 2", part_2)
