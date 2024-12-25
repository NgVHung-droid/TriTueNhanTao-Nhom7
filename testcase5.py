import unittest
import time
from final import generate_maze, maze_to_graph, A_star

class TestPerformanceMultipleRuns(unittest.TestCase):

    def test_multiple_runs(self):
        # Đặt số lần kiểm thử và kích thước mê cung
        num_runs = 100
        rows, cols = 50, 70
        
        total_time = 0
        for _ in range(num_runs):
            # Tạo mê cung ngẫu nhiên
            maze = generate_maze(rows, cols)
            
            # Chọn điểm bắt đầu và đích hợp lệ
            start = None
            goal = None
            for r in range(rows):
                for c in range(cols):
                    if maze[r][c] == 0:  # Chỉ chọn ô đường đi
                        if start is None:
                            start = (r, c)
                        elif goal is None:
                            goal = (r, c)

            # Chuyển đổi mê cung thành đồ thị
            graph = maze_to_graph(maze)
            
            # Đo thời gian tìm đường trong một lần chạy
            start_time = time.time()
            
            # Tìm đường đi
            path, cost = A_star(graph, start, goal)
            
            end_time = time.time()
            
            # Cộng tổng thời gian cho tất cả các lần chạy
            total_time += (end_time - start_time)
        
        average_time = total_time / num_runs
        print(f"Thời gian trung bình cho {num_runs} lần chạy: {average_time:.4f} giây")
        
        # Kiểm tra thời gian trung bình có hợp lý hay không (giới hạn dưới 1 giây mỗi lần chạy)
        self.assertLess(average_time, 1, "Thời gian trung bình quá lâu!")

if __name__ == '__main__':
    unittest.main()
