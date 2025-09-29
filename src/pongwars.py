import pygame


class PongWars(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((480, 480))
        self.clock = pygame.time.Clock()
        self.delta = 0
        self.p1 = pygame.Vector2(260, 200)
        self.p2 = pygame.Vector2(200, 260)
        self.side1 = 'bottom_right'
        self.side2 = 'top_left'
        self.running = True
        self.matrix = [
            {'x': x, 'y': y, 'color': 'black' if x >= 240 else 'grey'}
            for y in range(0, 480, 20) for x in range(0, 480, 20)]

    def exec(self):
        pygame.init()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.draw_wall()
            pygame.draw.circle(self.screen, 'grey', self.p1, 20)
            pygame.draw.circle(self.screen, 'black', self.p2, 20)
            self.side1 = self.pos(self.p1, self.side1, self.delta, 'grey')
            self.side2 = self.pos(self.p2, self.side2, self.delta, 'black')
            pygame.display.flip()
            self.delta = self.clock.tick(60) / 100
        pygame.quit()

    def draw_wall(self):
        for m in self.matrix:
            pygame.draw.rect(
                self.screen, m['color'], pygame.Rect(m['x'], m['y'], 20, 20))


    def pos(self, player, dire, d, color):
        player.y = player.y + 40 * d if 'bo' in dire else player.y - 40 * d
        player.x = player.x + 40 * d if 'ri' in dire else player.x - 40 * d
        if player.x >= 480:
            dire = dire.replace('right', 'left')
        if player.x <= 0:
            dire = dire.replace('left', 'right')
        if player.y >= 480:
            dire = dire.replace('bottom', 'top')
        if player.y <= 0:
            dire = dire.replace('top', 'bottom')


        # ix, iy = int(player.x // 20), int(player.y // 20)
        # m = self.matrix[iy * 24 + ix]

        ix = min(int(player.x // 20), 23)
        iy = min(int(player.y // 20), 23)
        m = self.matrix[iy * 24 + ix]

        if m['color'] == color:  # mesma cor que o player
            if 'right' in dire:
                dire = dire.replace('right', 'left')
            elif 'left' in dire:
                dire = dire.replace('left', 'right')

        m['color'] = 'grey' if color == 'black' else 'black'

        # for m in self.matrix:
        #     if player.x > m['x'] and player.x < m['x'] + 40:
        #         if player.y > m['y'] and player.y < m['y'] + 40:
        #             if m['color'] == color:
        #                 if 'right' in dire:
        #                     dire = dire.replace('right', 'left')
        #                 elif 'left' in dire:
        #                     dire = dire.replace('left', 'right')
        #                 m['color'] = 'grey' if color == 'black' else 'black'
        #             break

        return dire


if __name__ == '__main__':
    PongWars().exec()
