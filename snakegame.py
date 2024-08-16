import pygame
import time
import random

# Inicializa o Pygame
pygame.init()

# Define as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Define as dimensões da tela
largura_display = 800
altura_display = 600

# Cria a tela do jogo
display = pygame.display.set_mode((largura_display, altura_display))
pygame.display.set_caption('Jogo da Cobrinha')

# Configura o relógio do jogo
clock = pygame.time.Clock()
tamanho_cobra = 10
velocidade_cobra = 15

# Define a fonte para as mensagens
fonte = pygame.font.SysFont(None, 35)

# Função para desenhar a cobrinha
def nossa_cobra(tamanho_cobra, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(display, branco, [x[0], x[1], tamanho_cobra, tamanho_cobra])

# Função para exibir mensagens na tela
def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    display.blit(texto, [largura_display / 6, altura_display / 3])

# Função principal do jogo
def jogo():
    game_over = False
    game_close = False

    # Posição inicial da cobrinha
    x1 = largura_display / 2
    y1 = altura_display / 2

    # Mudança na posição da cobrinha
    x1_mudanca = 0
    y1_mudanca = 0

    # Lista para armazenar as posições da cobrinha
    lista_cobra = []
    comprimento_cobra = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura_display - tamanho_cobra) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_display - tamanho_cobra) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(preto)
            mensagem("Você perdeu! Pressione Q-Quit ou C-Continue", vermelho)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_cobra
                    y1_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_cobra
                    y1_mudanca = 0
                elif event.key == pygame.K_UP:
                    y1_mudanca = -tamanho_cobra
                    x1_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_cobra
                    x1_mudanca = 0

        # Verifica se a cobrinha bateu na parede
        if x1 >= largura_display or x1 < 0 or y1 >= altura_display or y1 < 0:
            game_close = True
        x1 += x1_mudanca
        y1 += y1_mudanca
        display.fill(preto)
        pygame.draw.rect(display, vermelho, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])
        cabeça_cobra = []
        cabeça_cobra.append(x1)
        cabeça_cobra.append(y1)
        lista_cobra.append(cabeça_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Verifica se a cobrinha bateu em si mesma
        for x in lista_cobra[:-1]:
            if x == cabeça_cobra:
                game_close = True

        nossa_cobra(tamanho_cobra, lista_cobra)
        pygame.display.update()

        # Verifica se a cobrinha comeu a comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura_display - tamanho_cobra) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_display - tamanho_cobra) / 10.0) * 10.0
            comprimento_cobra += 1

        clock.tick(velocidade_cobra)

    pygame.quit()
    quit()

jogo()
