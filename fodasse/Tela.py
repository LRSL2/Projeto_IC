import pygame

class Tela_inicial:
    tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    largura, altura = tela.get_size()
    pygame.display.set_caption("Tela de Login")

class Tela_jogo:
    largura = 1280
    altura = 720