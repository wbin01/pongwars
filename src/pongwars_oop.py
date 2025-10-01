import pygame


class PongWars(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((480, 480))
        self.clock, self.dt = pygame.time.Clock(), 0
        self.p1, self.p2 = pygame.Vector2(260, 200), pygame.Vector2(200, 260)
        self.side1, self.side2 = 'br', 'tl'
        self.mx = [{'x': x, 'y': y, 'cor': 'black' if x >= 220 else 'gold4'}
            for y in range(0, 480, 20) for x in range(0, 480, 20)]
        self.running = True, pygame.init()
    
    def exec(self):
        while self.running:
            self.running = all(
                event.type != pygame.QUIT for event in pygame.event.get())

            [pygame.draw.rect(self.screen, m['cor'], (m['x'], m['y'], 20, 20))
                for m in self.mx]
            pygame.draw.circle(self.screen, 'gold4', self.p1, 10)
            pygame.draw.circle(self.screen, 'black', self.p2, 10)
            self.side1 = self.hit(self.p1, self.side1, self.dt, 'gold4')
            self.side2 = self.hit(self.p2, self.side2, self.dt, 'black')
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 80
        pygame.quit()

    def hit(self, player, dire, d, color):
        player.y += 20 * self.dt if 'b' in dire else - 20 * self.dt
        player.x += 20 * self.dt if 'r' in dire else - 20 * self.dt
        dire = dire.replace('r', 'l') if player.x >= 480 else dire
        dire = dire.replace('l', 'r') if player.x <= 0 else dire
        dire = dire.replace('b', 't') if player.y >= 480 else dire
        dire = dire.replace('t', 'b') if player.y <= 0 else dire
        for m in self.mx:
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


if __name__ == '__main__':
    PongWars().exec()
