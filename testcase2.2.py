import unittest
from final import generate_maze

class TestValidStartGoal(unittest.TestCase):

    def test_start_and_goal_validity(self):
        # Tạo một mê cung ngẫu nhiên
        maze = generate_maze(50, 70)
        
        # Chọn điểm bắt đầu và điểm kết thúc hợp lệ
        start = None
        goal = None
        for r in range(50):
            for c in range(70):
                if maze[r][c] == 0:  # Chỉ có thể chọn ô đường đi (trắng)
                    if start is None:
                        start = (r, c)
                    elif goal is None:
                        goal = (r, c)

        # Đảm bảo ô bắt đầu và ô đích là ô đường đi
        self.assertEqual(maze[start[0]][start[1]], 0, "Ô bắt đầu không phải là ô đường đi!")
        self.assertEqual(maze[goal[0]][goal[1]], 0, "Ô đích không phải là ô đường đi!")

    def test_invalid_start_goal(self):
        # Tạo một mê cung ngẫu nhiên
        maze = generate_maze(50, 70)
        
        # Thử chọn một ô tường làm ô bắt đầu và đích
        start = (0, 0)  # Ô tường ở góc trên trái
        goal = (49, 69)  # Ô tường ở góc dưới phải
        
        self.assertNotEqual(maze[start[0]][start[1]], 0, "Ô bắt đầu không phải là ô đường đi!")
        self.assertNotEqual(maze[goal[0]][goal[1]], 0, "Ô đích không phải là ô đường đi!")

if __name__ == '__main__':
    unittest.main()
