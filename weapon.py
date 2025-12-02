from sprite_object import *


class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/shotgun/0.bmp', scale=0.4, animated_time=90):
        super().__init__(game=game, path=path, scale=scale, animeted_time=animated_time)
        self.images = deque([pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale)) for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def updarte(self):
        pass