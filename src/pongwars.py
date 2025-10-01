import pygame


def hit(player, dire, dt, color):
    player.y += 20 * dt if 'b' in dire else - 20 * dt
    player.x += 20 * dt if 'r' in dire else - 20 * dt
    dire = dire.replace('r', 'l') if player.x >= 480 else dire
    dire = dire.replace('l', 'r') if player.x <= 0 else dire
    dire = dire.replace('b', 't') if player.y >= 480 else dire
    dire = dire.replace('t', 'b') if player.y <= 0 else dire
    for m in mx:
        if player.x > m['x'] and player.x < m['x'] + 20:
            if player.y > m['y'] and player.y < m['y'] + 20:
                if m['cor'] == color:
                    if 'r' in dire:
                        dire = dire.replace('r', 'l')
                    elif 'l' in dire:
                        dire = dire.replace('l', 'r')
                    m['cor'] = 'gold4' if color == 'black' else 'black'
                break
    return dire

screen = pygame.display.set_mode((480, 480))
clock, dt = pygame.time.Clock(), 0
p1, p2 = pygame.Vector2(260, 200), pygame.Vector2(200, 260)
side1, side2 = 'br', 'tl'  # br=bottom_right, tl=top_left
mx = [{'x': x, 'y': y, 'cor': 'black' if x >= 240 else 'gold4'}
    for y in range(0, 480, 20) for x in range(0, 480, 20)]

running = True, pygame.init()
while running:
    running = all(event.type != pygame.QUIT for event in pygame.event.get())
    [pygame.draw.rect(screen, m['cor'], (m['x'], m['y'], 20, 20)) for m in mx]
    pygame.draw.circle(screen, 'gold4', p1, 10)
    pygame.draw.circle(screen, 'black', p2, 10)
    side1, side2 = hit(p1, side1, dt, 'gold4'), hit(p2, side2, dt, 'black')
    pygame.display.flip()
    dt = clock.tick(60) / 80

pygame.quit()
