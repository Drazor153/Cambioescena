import scene
import pygame
from pygame.locals import*

WIDTH = 640
HEIGHT = 480

class Pong(scene.Scene):
    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.bola = self.Bola()
        self.pala_jug = self.Pala(30)
        self.pala_cpu = self.Pala(WIDTH - 30)
        self.background_image = load_image("fondo_pong.png")
        self.puntos = [0, 0]

        
    def on_update(self, time):
        self.puntos = self.bola.actualizar(time, self.pala_jug, self.pala_cpu, self.puntos)
        self.pala_jug.mover(time, self.keys)
        self.pala_cpu.ia(time, self.bola)

        self.p_jug, self.p_jug_rect = texto(str(self.puntos[0]), WIDTH/4, 40)
        self.p_cpu, self.p_cpu_rect = texto(str(self.puntos[1]), WIDTH-WIDTH/4, 40)

        pass
 
    def on_event(self):
        self.keys = pygame.key.get_pressed()
        pass
 
    def on_draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        screen.blit(self.p_jug, self.p_jug_rect)
        screen.blit(self.p_cpu, self.p_cpu_rect)
        screen.blit(self.bola.image, self.bola.rect)
        screen.blit(self.pala_jug.image, self.pala_jug.rect)
        screen.blit(self.pala_cpu.image, self.pala_cpu.rect)
        pass

    class Pala(pygame.sprite.Sprite):
        def __init__(self, x):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image("pala.png")
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = HEIGHT/2
            self.speed = 0.5

        def mover(self, time, keys):
            if self.rect.top >= 0:
                if keys[K_UP]:
                    self.rect.centery -= self.speed*time

            if self.rect.bottom <= HEIGHT:
                if keys[K_DOWN]:
                    self.rect.centery += self.speed*time

        def ia(self, time, ball):
            if ball.speed[0] >= 0 and ball.rect.centerx >= WIDTH/2:
                if self.rect.centery < ball.rect.centery:
                    self.rect.centery += self.speed*time
                if self.rect.centery > ball.rect.centery:
                    self.rect.centery -= self.speed*time
    
    class Bola(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = load_image("ball.png", True)
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT/2
            self.speed = [0.5, -0.5]

        def actualizar(self, time, pala_jug, pala_cpu, puntos):
            self.rect.centerx += self.speed[0] * time
            self.rect.centery += self.speed[1] * time

            if self.rect.left <= 0:
                puntos[1] += 1
            if self.rect.right >= WIDTH:
                puntos[0] += 1

            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0] * time
            if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
                self.speed[1] = -self.speed[1]
                self.rect.centery += self.speed[1] * time

            if pygame.sprite.collide_rect(self, pala_jug):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0]*time

            if pygame.sprite.collide_rect(self, pala_cpu):
                self.speed[0] = -self.speed[0]
                self.rect.centerx += self.speed[0]*time

            return puntos



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

def texto(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font("DroidSans.ttf", 25)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect
