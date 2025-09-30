import pygame


def pos(player, dire, dt, color):
    player.y = player.y + 40 * dt if 'bo' in dire else player.y - 40 * dt
    player.x = player.x + 40 * dt if 'ri' in dire else player.x - 40 * dt
    if player.x >= 480:
        dire = dire.replace('right', 'left')
    if player.x <= 0:
        dire = dire.replace('left', 'right')
    if player.y >= 480:
        dire = dire.replace('bottom', 'top')
    if player.y <= 0:
        dire = dire.replace('top', 'bottom')

    for m in matrix:
        if player.x > m['x'] and player.x < m['x'] + 40:
            if player.y > m['y'] and player.y < m['y'] + 40:
                if m['color'] == color:
                    if 'right' in dire:
                        dire = dire.replace('right', 'left')
                    elif 'left' in dire:
                        dire = dire.replace('left', 'right')
                    m['color'] = 'gold4' if color == 'black' else 'black'
                break
    return dire

screen = pygame.display.set_mode((480, 480))
clock, dt = pygame.time.Clock(), 0
p1, p2 = pygame.Vector2(260, 200), pygame.Vector2(200, 260)
side1, side2 = 'bottom_right', 'top_left'
matrix = [{'x': x, 'y': y, 'color': 'black' if x >= 240 else 'gold4'}
    for y in range(0, 480, 20) for x in range(0, 480, 20)]

running, _ = True, pygame.init()
while running:
    for event in pygame.event.get():
            running = False if event.type == pygame.QUIT else True

    for m in matrix:
        pygame.draw.rect(
            screen, m['color'], pygame.Rect(m['x'], m['y'], 20, 20))

    pygame.draw.circle(screen, 'gold4', p1, 20)
    pygame.draw.circle(screen, 'black', p2, 20)
    side1, side2 = pos(p1, side1, dt, 'gold4'), pos(p2, side2, dt, 'black')
    pygame.display.flip()
    dt = clock.tick(60) / 100

pygame.quit()
