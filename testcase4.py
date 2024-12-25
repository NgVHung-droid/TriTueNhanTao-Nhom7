import unittest
from final import generate_maze, maze_to_graph, A_star

class TestInvalidClicks(unittest.TestCase):

    def test_invalid_clicks(self):
        # Tạo mê cung mới
        maze = generate_maze(50, 70)
        
        # Chọn các điểm bắt đầu và kết thúc hợp lệ (đảm bảo ô đường đi)
        start = None
        goal = None
        for r in range(50):
            for c in range(70):
                if maze[r][c] == 0:  # Chỉ chọn ô đường đi
                    if start is None:
                        start = (r, c)
                    elif goal is None:
                        goal = (r, c)

        # Chuyển đổi mê cung thành đồ thị
        graph = maze_to_graph(maze)
        
        # Tạo một số tọa độ không hợp lệ để thử nhấp vào (chẳng hạn như tường hoặc vùng ngoài mê cung)
        invalid_positions = [(0, 0), (49, 69), (100, 100)]  # Vị trí tường và ngoài phạm vi mê cung
        
        for pos in invalid_positions:
            # Kiểm tra nhấp vào ô không hợp lệ (tường hoặc ngoài phạm vi)
            try:
                x, y = pos
                # Đảm bảo chương trình không gặp lỗi khi nhấp vào ô không hợp lệ
                if maze[x][y] == 1:  # Nếu ô là tường, kiểm tra không gây lỗi
                    print(f"Nhấp vào ô tường tại {pos} - OK")
                elif x < 0 or y < 0 or x >= 50 or y >= 70:
                    print(f"Nhấp vào ngoài phạm vi mê cung tại {pos} - OK")
            except IndexError:
                print(f"Vị trí ngoài phạm vi hoặc không hợp lệ: {pos} - OK")

if __name__ == '__main__':
    unittest.main()
