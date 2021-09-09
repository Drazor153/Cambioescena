import scene
import pygame
from pygame.locals import*

WIDTH = 640
HEIGHT = 480


class Menu(scene.Scene):
    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.background_image = load_image("fondo_pong.png")
        self.btn_menu = self.b_Menu()
        
    def on_update(self, time):
        pass
 
    def on_event(self):
        if self.btn_menu.is_clicked():
            self.director.change_scene(self.director.scenes[1])
        pass
 
    def on_draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        screen.blit(self.btn_menu.image, self.btn_menu.rect)
        pass
    
    class b_Menu(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image("menu.png")
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT/2
        
        def is_clicked(self):
            return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

def load_image(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit
    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image
