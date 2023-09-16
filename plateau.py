from typing import Tuple
# milieu case de depart x:560 y:450
INDEX_X = 560
INDEX_Y = 450
def get_coords(x: int, y: int) -> Tuple[int, int]:
    x, y = x-1, y-1
    larg_x = 115
    new_x = INDEX_X + x*larg_x + int(larg_x/2)*(y%2)
    new_y = INDEX_Y + y*75
    return new_x, new_y
print(get_coords(3, 4))