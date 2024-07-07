import pygame

class Player:
    def __init__(self, screen_width, screen_height, ground_height):
        self.width = 15
        self.height = 20
        self.x = 50
        self.y = screen_height - ground_height - self.height
        self.speed = 8
        self.is_jumping = False
        self.gravity = 2
        self.jump_height = 15
        self.jump_velocity = self.jump_height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ground_height = ground_height
        self.color = (255, 0, 0)

    def update(self, keys, fragments):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_SPACE] and not self.is_jumping and not fragments.is_active:
            self.is_jumping = True
            self.jump_velocity = -self.jump_height

        if self.is_jumping:
            self.y += self.jump_velocity
            self.jump_velocity += self.gravity
            if self.y >= self.screen_height - self.ground_height - self.height:
                self.y = self.screen_height - self.ground_height - self.height
                self.is_jumping = False

        if self.x < 0:
            self.x = 0
        if self.x + self.width > self.screen_width:
            self.x = self.screen_width - self.width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def check_collision(self, obstacles):
        for obstacle_points in obstacles:
            obstacle_x = obstacle_points[0][0]
            obstacle_y = obstacle_points[1][1]
            if self.x < obstacle_x + 10 and self.x + self.width > obstacle_x and \
               self.y < obstacle_y + 20 and self.y + self.height > obstacle_y:
                return True
        return False

    def reset(self):
        self.x = 50
        self.y = self.screen_height - self.ground_height - self.height
