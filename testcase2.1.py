import unittest
import random
from final import generate_maze, maze_to_graph, A_star

class TestRandomMaze(unittest.TestCase):

    def test_maze_structure(self):
        # Tạo một mê cung ngẫu nhiên
        maze = generate_maze(50, 70)
        
        # Đảm bảo mê cung có ít nhất một đường đi
        start_found = False
        goal_found = False
        for row in maze:
            for cell in row:
                if cell == 0:  # Cell đường đi
                    start_found = True
                    break
        self.assertTrue(start_found, "Không tìm thấy ô đường đi trong mê cung!")

    def test_maze_path_exists(self):
        # Tạo một mê cung ngẫu nhiên và chuyển đổi thành đồ thị
        maze = generate_maze(50, 70)
        graph = maze_to_graph(maze)
        
        # Chọn điểm bắt đầu và đích trong mê cung
        start = (0, 0)
        goal = (49, 69)
        
        # Đảm bảo có ít nhất một đường đi từ bắt đầu đến kết thúc
        path, _ = A_star(graph, start, goal)
        self.assertIsNotNone(path, "Không tìm thấy đường đi từ bắt đầu đến kết thúc!")

if __name__ == '__main__':
    unittest.main()
