import unittest
from final import generate_maze, maze_to_graph, A_star

class TestNoPathFound(unittest.TestCase):

    def test_no_path(self):
        # Tạo một mê cung ngẫu nhiên
        maze = generate_maze(50, 70)
        
        # Chọn các điểm bắt đầu và kết thúc sao cho không có đường đi (chọn tường để chặn)
        start = (0, 0)  # Chọn ô góc trên trái
        goal = (49, 69)  # Chọn ô góc dưới phải
        
        # Chuyển đổi mê cung thành đồ thị
        graph = maze_to_graph(maze)
        
        # Giả lập tình huống không có đường đi
        maze[start[0]][start[1]] = 1  # Đặt điểm bắt đầu thành tường
        maze[goal[0]][goal[1]] = 1  # Đặt điểm kết thúc thành tường
        
        # Tìm đường đi bằng thuật toán A*
        path, cost = A_star(graph, start, goal)
        
        # Đảm bảo không tìm được đường đi
        self.assertIsNone(path, "Không xử lý trường hợp không tìm được đường đi!")
        
        # Đảm bảo không có đường đi nào được tô màu
        self.assertEqual(cost, float('inf'), "Chi phí không phải là vô cùng!")

        # In thông báo khi không tìm thấy đường đi
        print("No Path Found!")

if __name__ == '__main__':
    unittest.main()
