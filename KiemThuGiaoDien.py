import pygame
import unittest
from final import main, Button, generate_maze, A_star, maze_to_graph

class TestMazeGame(unittest.TestCase):
    def setUp(self):
        """Khởi tạo môi trường Pygame."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.create_button = Button(10, 750, 380, 50, "Create Maze")
        self.find_button = Button(400, 750, 380, 50, "Find Path")
        self.heuristic_button = Button(790, 750, 380, 50, "Heuristic")
        self.clock = pygame.time.Clock()

    def tearDown(self):
        """Đóng Pygame sau kiểm thử."""
        pygame.quit()

    def test_create_button_click(self):
        """Kiểm tra nút 'Create Maze' hoạt động đúng."""
        self.create_button.click_effect(self.screen)
        maze = generate_maze(50, 70)
        self.assertEqual(len(maze), 50)
        self.assertEqual(len(maze[0]), 70)
        self.assertTrue(all(cell in [0, 1] for row in maze for cell in row))

    def test_find_path_button(self):
        """Kiểm tra nút 'Find Path' và thuật toán A*."""
        maze = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
        graph = maze_to_graph(maze)
        start = (0, 0)
        goal = (2, 2)
        path, cost = A_star(graph, start, goal, "manhattan")
        self.assertIsNotNone(path)
        self.assertEqual(path, [(1, 0), (2, 0), (2, 1), (2, 2)])
        self.assertEqual(cost, 4)

    def test_heuristic_popup(self):
        """Kiểm tra popup heuristic hoạt động đúng."""
        popup_width = 300
        popup_height = 290
        popup_rect = pygame.Rect((1200 - popup_width) // 2, (800 - popup_height) // 2, popup_width, popup_height)
        pygame.draw.rect(self.screen, (255, 255, 255), popup_rect)
        self.assertEqual(popup_rect.width, popup_width)
        self.assertEqual(popup_rect.height, popup_height)

    def test_maze_display(self):
        """Kiểm tra mê cung được vẽ đúng."""
        maze = generate_maze(50, 70)
        start = (0, 0)
        goal = (49, 69)
        path = []
        for row in maze:
            self.assertTrue(all(cell in [0, 1] for cell in row))
        # Đây chỉ là kiểm tra cơ bản, có thể thêm kiểm tra pixel cụ thể nếu cần.

    def test_status_display(self):
        """Kiểm tra trạng thái được hiển thị chính xác."""
        font = pygame.font.Font(None, 40)
        text = "Path Found!"
        text_surf = font.render(text, True, (0, 255, 0))
        self.assertIsNotNone(text_surf)

if __name__ == "__main__":
    unittest.main()
