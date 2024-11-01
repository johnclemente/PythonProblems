# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
gravity_bomb_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
orb_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # set screen and UI
    screen.fill("black")
    screen_width, screen_height = screen.get_size()
    font = pygame.font.Font(None, 75)
    text_color = (255, 0, 0)

    # hide mouse
    pygame.mouse.set_visible(False)

    # make characters
    # gravity_bomb = pygame.draw.circle(screen, "white", gravity_bomb_pos, 40)

    player = pygame.draw.circle(screen, "blue", player_pos, 40)
    player_radius = 30

    orb = pygame.draw.circle(screen, "red", orb_pos, 20)

    # move player with cursor
    player_pos = pygame.mouse.get_pos()
    
    # player 2 movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        orb_pos.y -= 600 * dt
    if keys[pygame.K_s]:
        orb_pos.y += 600 * dt
    if keys[pygame.K_a]:
        orb_pos.x -= 600 * dt
    if keys[pygame.K_d]:
        orb_pos.x += 600 * dt
        
    def gameOver():
        game_over_text = font.render("You Lose", True, text_color)
        text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
        #blit(source, destination)
        screen.fill("white")
        screen.blit(game_over_text,text_rect)

    if (player_pos[1] - player_radius < 0 or player_pos[1] + player_radius >= screen_height or player_pos[0] - player_radius < 0 or player_pos[0] + player_radius >= screen_width):
        gameOver()
    if abs(player_pos[0] - orb_pos[0]) <= player_radius and abs(player_pos[1] - orb_pos[1]) <= player_radius:
        gameOver()


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
