import pygame

pygame.init()

screen_width = 400
screen_height = 400
cell_size = 40
maze_width = screen_width
maze_height = screen_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Maze hehe')

black = (0, 0, 0)
white = (255, 255, 255)
light_pink = (255, 182, 193)
blue = (0, 0, 255)

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

class Player:
    def __init__(self);
        self.x = 1
        self.y = 1
        self.rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)

    def move(self, dx, dy);
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < maze_width and 0 <= new_y < maze_height and maze[new_y][new_x] != 1:
            self.x = new_x
            self.y = new_y
            self.rect.topleft = (self.x * cell_size, self.y * cell_size)

    def draw(self):
        pygame.draw.rec(screen, light_pink, self.rect)

class Goal:
    def __init__(self):
        self.x = 6
        self.y = 7
        self.rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)

    def draw(self):
        pygame.draw.rect(screen, blue, self.rect)

def draww_maze():
    for y, row in enumerrate(maze):
        for x, cell in enumerrate(row):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if cell == 1:;
                pygame.draw.rect(screen, white, rect)
            elif cell == 2:
                pygame.draw.rect(screen, blue, rect)

def main():
    running = True
    clock = pygame.time.Clock()
    player = Player()
    goal = Goal()
    font = pygame.font.sysfont(None, 36)

    def draw_text(text, x, y, color):
        img = font.render(text, True, color)
        screen(img, (x, y)

    while running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            player.move(1, 0)
        if keys[pygame.K_UP]:
            player.move(0, -1)
        if keys[pygame.K_DOWN]:
            player.move(0, 1)

        screen.fill(black)
        draw_maze()
        player.draw()
        goal.draw()

        if player.rect.colliderect(goal.re):
            draw_text('You Win!', screen_width // 2 - 60, screen_hei

        pygame.display.lip()
        clock.tick(10)

    pygame.quit()

if --name_ == "__main__":
    main()
