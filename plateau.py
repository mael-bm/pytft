from typing import Tuple

# milieu case de depart x:560 y:450
INDEX_X = 560
INDEX_Y = 450


# x -> 1..7, y -> 1..4
def get_coords(x: int, y: int) -> Tuple[int, int]:
    x, y = x - 1, y - 1
    size_x = 115 + y * 3
    new_x = INDEX_X + x * size_x + int(size_x / 2.2) * (y % 2) - 20*(y-1)
    if y == 3:
        new_x += 10
        if x >= 3:
            new_x += 13
    new_y = INDEX_Y + y * 71
    return new_x, new_y


# print(get_coords(7, 4))
