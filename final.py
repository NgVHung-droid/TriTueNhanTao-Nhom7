import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1200, 800
ROWS, COLS = 50, 70
BUTTON_HEIGHT = 50
MAZE_HEIGHT = HEIGHT - BUTTON_HEIGHT

CELL_SIZE = min(WIDTH // COLS, MAZE_HEIGHT // ROWS)
maze_width = CELL_SIZE * COLS
maze_height = CELL_SIZE * ROWS

WHITE = (255, 255, 255) #màu đường đi
BLACK = (0, 0, 0) #màu tường
RED = (255, 0, 0) # màu điểm đích
BLUE = (0, 0, 255) # màu đường đi tối ưu
GREEN = (0, 255, 0) # màu ô start
YELLOW = (255, 255, 0) # các ô tập MO
ORANGE = (255, 165, 0) # các ô tập DONG
GRAY = (200, 200, 200)
BUTTON_COLOR = (50, 150, 200)
BUTTON_TEXT_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("20241IT6094003 - Nhóm 7 - Giải Mê Cung Dùng A*")

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = BUTTON_COLOR
        self.clicked_color = (100, 200, 255)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surf = font.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def click_effect(self, screen):
        original_color = self.color
        self.color = self.clicked_color
        self.draw(screen)
        pygame.display.flip()
        pygame.time.delay(100) 
        self.color = original_color


def generate_maze(rows, cols):
    maze = [[1 if random.random() < 0.7 else 0 for _ in range(cols)] for _ in range(rows)]
    return maze


def draw_maze(maze, start, goal, path):
    offset_x = (WIDTH - maze_width) // 2
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            color = WHITE if maze[r][c] == 1 else BLACK
            if (r, c) == start:
                color = GREEN
            elif (r, c) == goal:
                color = RED
            elif (r, c) in path:
                color = BLUE
            pygame.draw.rect(
                screen,
                color,
                (offset_x + c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1),
            )


def draw_cell(cell, color):
    r, c = cell
    offset_x = (WIDTH - maze_width) // 2
    pygame.draw.rect(
        screen,
        color,
        (offset_x + c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1),
    )


def h(n, goal):
    return abs(n[0] - goal[0]) + abs(n[1] - goal[1])


def maze_to_graph(maze):
    graph = {}
    rows, cols = len(maze), len(maze[0])
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                neighbors = []
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 1:
                        neighbors.append(((nr, nc), 1))
                graph[(r, c)] = neighbors
    return graph


def A_star(graph, start, goal):
    MO = [start]
    DONG = []
    g = {start: 0}
    f = {start: h(start, goal)}
    parent = {}

    while MO:
        for node in MO:
            if node != start and node != goal:
                draw_cell(node, YELLOW)
        for node in DONG:
            if node != start and node != goal:
                draw_cell(node, ORANGE)
        pygame.display.flip()
        pygame.time.delay(10)

        n = min(MO, key=lambda node: f[node])

        if n == goal:
            path = []
            while n != start:
                path.append(n)
                n = parent[n]
            path.reverse()
            for cell in path:
                if cell != start and cell != goal:
                    draw_cell(cell, BLUE)
                    pygame.display.flip()
                    pygame.time.delay(30)
            return path, g[goal]

        MO.remove(n)
        DONG.append(n)

        for m, cost in graph.get(n, []):
            cost_g_new = g[n] + cost
            if m not in MO and m not in DONG:
                g[m] = cost_g_new
                f[m] = g[m] + h(m, goal)
                parent[m] = n
                MO.append(m)
            elif m in MO and g[m] > cost_g_new:
                g[m] = cost_g_new
                f[m] = g[m] + h(m, goal)
                parent[m] = n

    return None, float('inf')


def main():
    clock = pygame.time.Clock()
    maze = generate_maze(ROWS, COLS)
    start, goal = None, None
    path = []

    button_width = (WIDTH - 40) // 2
    create_button = Button(10, HEIGHT - BUTTON_HEIGHT, button_width - 10, BUTTON_HEIGHT, "Create Maze")
    find_button = Button(button_width + 20, HEIGHT - BUTTON_HEIGHT, button_width - 10, BUTTON_HEIGHT, "Find Path")

    running = True
    while running:
        screen.fill(GRAY)
        draw_maze(maze, start, goal, path)
        create_button.draw(screen)
        find_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if create_button.is_clicked(pos):
                    create_button.click_effect(screen)
                    maze = generate_maze(ROWS, COLS)
                    start, goal, path = None, None, []
                elif find_button.is_clicked(pos) and start and goal:
                    find_button.click_effect(screen)  
                    graph = maze_to_graph(maze)
                    path, cost = A_star(graph, start, goal)
                    if path is None:
                        path = []  
                        print("Không tìm thấy đường đi!")
                        font = pygame.font.Font(None, 40)
                        text_surf = font.render("No Path Found !", True, RED)
                        text_rect = text_surf.get_rect(center=(WIDTH // 2, HEIGHT - BUTTON_HEIGHT // 2))
                        screen.blit(text_surf, text_rect)
                        pygame.display.flip()
                        pygame.time.wait(1500)
                    else:
                        print(f"Đường đi: {path}")
                        print(f"Chi phí: {cost}")
                else:
                    x, y = pos
                    offset_x = (WIDTH - maze_width) // 2
                    if offset_x <= x < offset_x + maze_width and y < maze_height:
                        r, c = y // CELL_SIZE, (x - offset_x) // CELL_SIZE
                        if r < ROWS and c < COLS and maze[r][c] == 1:
                            if start is None:
                                start = (r, c)
                            elif goal is None:
                                goal = (r, c)
                            else:
                                start, goal, path = (r, c), None, []

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
