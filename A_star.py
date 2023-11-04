from queue import PriorityQueue


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_neighbors(self):
        return [
            Cell(self.x + 1, self.y),
            Cell(self.x - 1, self.y),
            Cell(self.x, self.y + 1),
            Cell(self.x, self.y - 1)
        ]

    def __lt__(self, other):
        return False

    def __eq__(self, other):
        return isinstance(other, Cell) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


# Манхеттонское расстояние
def heuristic(cell1, cell2):
    return abs(cell1.x - cell2.x) + abs(cell1.y - cell2.y)


def find_path(start, goal, obstacles):
    if start in obstacles or goal in obstacles:
        print("Путь не может быть найден. Начальная или конечная точка находится в списке препятствий.")
        return []

    open_set = PriorityQueue()  # открытый список узлов
    open_set.put((0, start))
    came_from = {}  # словарь родительских узлов
    g_score = {start: 0}  # словарь текущих оценок стоимостей перемещения
    closed_set = set()  # закрытый список узлов

    while not open_set.empty():
        current = open_set.get()[1]
        if current == goal:
            break

        closed_set.add(current)

        neighbors = current.get_neighbors()

        for neighbor in neighbors:
            if neighbor in obstacles or neighbor in closed_set:
                continue

            new_g_score = g_score[current] + 1
            if neighbor not in g_score or new_g_score < g_score[neighbor]:
                g_score[neighbor] = new_g_score
                f_score = new_g_score + heuristic(neighbor, goal)
                open_set.put((f_score, neighbor))
                came_from[neighbor] = current

    if goal not in came_from:
        print("Путь не может быть найден.")
        return []

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path


start = Cell(0, 2)
goal = Cell(4, 4)

cell_list = [
    Cell(0, 0),
    Cell(0, 1),
    Cell(0, 2),
    Cell(0, 3),
    Cell(0, 4),
    Cell(1, 0),
    Cell(1, 1),
    Cell(1, 2),
    Cell(1, 3),
    Cell(1, 4),
    Cell(2, 0),
    Cell(2, 1),
    Cell(2, 2),
    Cell(2, 3),
    Cell(2, 4),
    Cell(3, 0),
    Cell(3, 1),
    Cell(3, 2),
    Cell(3, 3),
    Cell(3, 4),
    Cell(4, 0),
    Cell(4, 1),
    Cell(4, 2),
    Cell(4, 3),
    Cell(4, 4)
]

obstacles = []

obstacles.append(cell_list[0])
obstacles.append(cell_list[1])
obstacles.append(cell_list[3])
obstacles.append(cell_list[4])

path = find_path(start, goal, obstacles)

pathway = [(cell.x, cell.y) for cell in path]

print(pathway)