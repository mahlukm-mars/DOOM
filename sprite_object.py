import pygame as pg
from settings import *

class SpriteObject:
    def __init__(self, game, path = 'resources/sprites/static_sprites/candlebra.bmp', pos=(10.5, 3.5)):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.distance, self.norm_distance = 0, 0, 0, 0, 1, 1   
        self.sprite_half_width = 0

    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_distance
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height))

        self.sprite_half_width = proj_width // 2
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2

        self.game.raycasting.objects_to_render.append((self.norm_distance, image, pos))

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (NUM_RAYS // 2 + delta_rays) * SCALE

        self.distance = math.hypot(dx, dy)
        self.norm_distance = self.distance * math.cos(delta)
        if -self.HALF_WIDTH < self.screen_x < (WIDTH + self.HALF_WIDTH) and self.norm_distance > 0.5:
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()
