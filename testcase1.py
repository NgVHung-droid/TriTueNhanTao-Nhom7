import unittest
import pygame
from final import Button

class TestButtons(unittest.TestCase):

    def setUp(self):
        # Khởi tạo pygame và màn hình kiểm thử
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))

    def tearDown(self):
        # Đóng pygame sau khi kiểm thử
        pygame.quit()

    def test_create_maze_button(self):
        # Tạo nút "Create Maze"
        create_button = Button(10, 750, 580, 50, "Create Maze")
        
        # Vẽ nút và kiểm tra hiển thị
        create_button.draw(self.screen)
        pygame.display.flip()
        
        # Kiểm tra xem nút "Create Maze" có thể nhấp được không
        mouse_pos = (15, 755)  # Vị trí click trong khu vực của nút
        self.assertTrue(create_button.is_clicked(mouse_pos))  # Đảm bảo nút có thể nhấp

    def test_find_path_button(self):
        # Tạo nút "Find Path"
        find_button = Button(610, 750, 580, 50, "Find Path")
        
        # Vẽ nút và kiểm tra hiển thị
        find_button.draw(self.screen)
        pygame.display.flip()
        
        # Kiểm tra xem nút "Find Path" có thể nhấp được không
        mouse_pos = (615, 755)  # Vị trí click trong khu vực của nút
        self.assertTrue(find_button.is_clicked(mouse_pos))  # Đảm bảo nút có thể nhấp

if __name__ == '__main__':
    unittest.main()
