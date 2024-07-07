import pygame

def create_obstacles(screen_width, screen_height, ground_height):
    obstacle_width = 10
    obstacle_height = 20
    obstacle1_x_start = screen_width // 2 - (3 * obstacle_width) // 2 - 100
    obstacle2_x_start = screen_width // 2 + 200
    obstacles = []
    for obstacle_x_start in [obstacle1_x_start, obstacle2_x_start]:
        for j in range(3):
            obstacle_x = obstacle_x_start + j * obstacle_width
            obstacle_y = screen_height - ground_height - obstacle_height
            points = [(obstacle_x, obstacle_y + obstacle_height),
                      (obstacle_x + obstacle_width // 2, obstacle_y),
                      (obstacle_x + obstacle_width, obstacle_y + obstacle_height)]
            obstacles.append(points)
    return obstacles

def draw_obstacles(screen, obstacles):
    obstacle_color = (0, 0, 0)
    for obstacle_points in obstacles:
        pygame.draw.polygon(screen, obstacle_color, obstacle_points)
