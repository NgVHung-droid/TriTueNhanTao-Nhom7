import unittest
from final import generate_maze, maze_to_graph, A_star, h_manhattan, h_euclidean, h_chebyshev, h_octile


class TestMazeGenerator(unittest.TestCase):
    """Kiểm thử liên quan đến việc tạo mê cung."""
    def test_generate_maze(self):
        """Kiểm tra mê cung được tạo có kích thước đúng và giá trị hợp lệ."""
        rows, cols = 10, 15
        maze = generate_maze(rows, cols)
        self.assertEqual(len(maze), rows, "Số hàng không đúng.")
        self.assertTrue(all(len(row) == cols for row in maze), "Số cột không đúng.")
        self.assertTrue(all(cell in [0, 1] for row in maze for cell in row), "Giá trị ô không hợp lệ.")


class TestGraphConversion(unittest.TestCase):
    """Kiểm thử liên quan đến việc chuyển đổi mê cung sang đồ thị."""
    def test_maze_to_graph(self):
        """Kiểm tra chuyển đổi mê cung sang đồ thị."""
        maze = [
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 0],
        ]
        graph = maze_to_graph(maze)
        expected_keys = [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (2, 1)]
        self.assertCountEqual(graph.keys(), expected_keys, "Danh sách các đỉnh không đúng.")
        self.assertIn(((1, 0), 1), graph[(0, 0)], "Láng giềng không đúng.")


class TestHeuristics(unittest.TestCase):
    """Kiểm thử các hàm heuristic."""
    def test_h_manhattan(self):
        """Kiểm tra khoảng cách Manhattan."""
        self.assertEqual(h_manhattan((0, 0), (3, 4)), 7)
        self.assertEqual(h_manhattan((1, 2), (1, 2)), 0)

    def test_h_euclidean(self):
        """Kiểm tra khoảng cách Euclidean."""
        self.assertAlmostEqual(h_euclidean((0, 0), (3, 4)), 5.0, places=1)
        self.assertEqual(h_euclidean((1, 2), (1, 2)), 0.0)

    def test_h_chebyshev(self):
        """Kiểm tra khoảng cách Chebyshev."""
        self.assertEqual(h_chebyshev((0, 0), (3, 4)), 4)
        self.assertEqual(h_chebyshev((1, 2), (1, 2)), 0)

    def test_h_octile(self):
        """Kiểm tra khoảng cách Octile."""
        self.assertAlmostEqual(h_octile((0, 0), (3, 4)), round(5.242640687119286, 3), places=3)
        self.assertEqual(h_octile((1, 2), (1, 2)), 0)


class TestAStarAlgorithm(unittest.TestCase):
    """Kiểm thử thuật toán A*."""
    def test_A_star_valid_path(self):
        """Kiểm tra thuật toán A* với trường hợp có đường đi."""
        maze = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
        graph = maze_to_graph(maze)
        start, goal = (0, 0), (2, 2)
        path, cost = A_star(graph, start, goal, "manhattan")
        self.assertEqual(path, [(1, 0), (2, 0), (2, 1), (2, 2)])
        self.assertEqual(cost, 4)

    def test_A_star_no_path(self):
        """Kiểm tra thuật toán A* với trường hợp không có đường đi."""
        maze = [
            [1, 0, 1],
            [0, 0, 1],
            [1, 1, 0],
        ]
        graph = maze_to_graph(maze)
        path, cost = A_star(graph, (0, 0), (2, 2), "manhattan")
        self.assertIsNone(path, "Không tìm thấy đường đi nhưng path không phải None.")
        self.assertEqual(cost, float('inf'), "Chi phí phải là vô cực khi không có đường đi.")


if __name__ == "__main__":
    unittest.main()
