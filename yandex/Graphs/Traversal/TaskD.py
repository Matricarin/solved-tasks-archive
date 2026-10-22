# выход из лабиринта: один ключ

import sys
from typing import List, Tuple

def get_linear_place(row: int, col: int, length:int):
    return row * length + col

def read_input() -> Tuple[int, int, List[str]]:
    start:int = 0
    end: int = 0
    with open('input.txt') as in_file:
        sys.stdin = in_file
        line_1 = input().split(sep=' ')
        (n, m) = (int(line_1[0]), int(line_1[1]))
        maze:List[str] = ["" for _ in range(n)]
        for x in range(n):
            row = input()
            maze[x] = row
            for y in range(m):
                if maze[x][y] == 'S':
                    start = get_linear_place(x, y, m)
                if maze[x][y] == 'F':
                    end =  get_linear_place(x, y, m)            
    return start, end, maze
    
def find_exit(start:int, end:int, maze:List[str]) -> Tuple[int, List[str]]:
    ...

def write_answer(path_length: int, steps: List[str]):
    with open('output.txt', 'w') as out_file:
        sys.stdout = out_file
        print(f"{path_length}\n{"".join(steps)}") 

def main():
    (start, end, maze) = read_input()
    (length, steps) = find_exit(start, end, maze)
    write_answer(length, steps)

if __name__ == "__main__":
    main()