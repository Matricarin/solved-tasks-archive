# выход из лабиринта

from collections import deque


def read_input() -> tuple[list[str], tuple[int, int], tuple[int, int]]:
    with open('input.txt') as in_file:
        line_1 = in_file.readline().split(sep=' ')
        (n, m) = (int(line_1[0]), int(line_1[1]))
        maze:list[str] = ["" for _ in range(n)]
        start: tuple[int, int] = (0, 0)
        end: tuple[int, int] = (0, 0)
            
        for x in range(n):
            row = in_file.readline()
            maze[x] = row
            for y in range(m):
                if maze[x][y] == 'S':
                    start = (x, y)
                if maze[x][y] == 'F':
                    end = (x, y)
    return maze, start, end 


def get_linear_place(row: int, col: int, length:int):
    return row * length + col

def analyze(maze: list[str], start:tuple[int, int], end:tuple[int, int]) -> tuple[int, list[str]]:
    parents = [(0, "") for x in range(len(maze) * len(maze[0]))]
    row_length = len(maze[0])
    start_inline = get_linear_place(start[0], start[1], row_length)
    end_inline = get_linear_place(end[0], end[1], row_length)
    parents[start_inline] = (0, "S")
    visited_cells: set = set()
    cells_queue: deque = deque()
    cells_queue.append(start)
    is_finding = True
    
    while len(cells_queue) > 0 and is_finding:
        cell = cells_queue.popleft()
        visited_cells.add(cell)
        neighbors =[(cell[0] - 1, cell[1], "U"),
                    (cell[0], cell[1] - 1, "L"),
                    (cell[0] + 1, cell[1], "D"),
                    (cell[0], cell[1] + 1, "R")]
        for neighbor in neighbors:
            if ((neighbor[0], neighbor[1]) not in visited_cells 
                and 0 <= neighbor[0] < len(maze) 
                and 0 <= neighbor[1] < len(maze[0])):
                match maze[neighbor[0]][neighbor[1]]:
                    case "#":
                        continue
                    case "F":                        
                        parents[get_linear_place(neighbor[0], neighbor[1], row_length)] = (
                            get_linear_place(cell[0], cell[1], row_length), neighbor[2])
                        is_finding = False
                        break
                    case ".":
                        cells_queue.append((neighbor[0], neighbor[1]))
                        parents[get_linear_place(neighbor[0], neighbor[1], row_length)] = (
                                get_linear_place(cell[0], cell[1], row_length), neighbor[2])
                            
    
    counter = 0
    path = []
    finding = True
    last = parents[end_inline]
    
    if parents[end_inline][1] not in ['L', 'R', 'D', 'U']:
        return -1, []
    
    while finding:
        if last[1] == 'S':
            finding = False
        else:
            counter+=1
            path.append(last[1])
            last = parents[last[0]]
    path.reverse()
    
    return counter, path


def write_solution(path_len:int, steps:list[str]):
    with open('output.txt', 'w') as out_file:
        if path_len == -1:
            out_file.write(str(-1))
        else:
            out_file.write(f'{path_len}\n{''.join(steps)}')

def main():
    maze, start, end = read_input()
    (path_len, steps) = analyze(maze, start, end)
    write_solution(path_len=path_len, steps=steps)

if __name__ == "__main__":
    main()