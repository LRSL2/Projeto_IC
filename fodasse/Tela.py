import pygame

class Tela:
    tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    largura, altura = tela.get_size()
    pygame.display.set_caption("Tela de Login")
