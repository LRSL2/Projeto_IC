import pygame
from Telas import Tela_inicial
pygame.init()

#classe botão
class Botao():
    def __init__(self, x, y, imagem_normal, imagem_selecionada):
        botao_img = pygame.image.load(imagem_normal).convert_alpha()              
        botao_selecionado_img = pygame.image.load(imagem_selecionada).convert_alpha()
        self.imagem_normal = botao_img
        self.imagem_selecionada = botao_selecionado_img
        self.imagem_atual = self.imagem_normal 
        self.rect = self.imagem_normal.get_rect(center=(x, y))
    

    def checar_hover(self, posicao_mouse):
        if self.rect.collidepoint(posicao_mouse):
            self.imagem_atual = self.imagem_selecionada
        else:
            self.imagem_atual = self.imagem_normal
    
    def desenhar(self, tela):
        tela.blit(self.imagem_atual, self.rect)


# --- Seção de carregamento e posicionamento ---
# Imagem de fundo
imagem_tela_start = pygame.transform.scale(pygame.image.load('Tela inicial.jpg').convert(), (Tela_inicial.largura, Tela_inicial.altura))


#criação dos botoes

botao_jogar = Botao(Tela_inicial.largura // 2, Tela_inicial.altura*0.7, 'Frame 2.png', 'Frame 14 (2).png')
botao_sair = Botao(Tela_inicial.largura // 2, Tela_inicial.altura*0.8, 'Frame 2 (1).png', 'Frame 13.png')


lista_de_botoes = [botao_jogar, botao_sair]

# --- Loop principal do jogo ---
rodando = True
while (rodando):
    posicao_mouse = pygame.mouse.get_pos()

    # --- Seção de Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        ### NOVO: Lógica de clique para o botão SAIR
        if event.type == pygame.MOUSEBUTTONDOWN:
            if botao_sair.rect.collidepoint(posicao_mouse):
                rodando = False # Fecha o jogo ao clicar em SAIR
            if botao_jogar.rect.collidepoint(posicao_mouse):
                print("Clicou em JOGAR! (Aqui você mudaria para a tela do jogo)")

    # --- Seção de Desenho ---
    Tela_inicial.tela.blit(imagem_tela_start, (0,0))

    # Desenha todos os botões da lista
    for botao in lista_de_botoes:
        botao.checar_hover(posicao_mouse)
        botao.desenhar(Tela_inicial.tela)

    pygame.display.flip()

pygame.quit()