import pygame
from random import randint

pygame.init()

# entre-pistas e placas
fundo = pygame.image.load('imagens/pista.png')
entrefaixas = pygame.image.load('imagens/entre-faixas.png')
placas = [pygame.image.load('imagens/placa1.png'),
          pygame.image.load('imagens/placa2.png'),
          pygame.image.load('imagens/placa3.png'),
          pygame.image.load('imagens/placa4.png')]
v1 = -12  # velocidade da peça entre pistas e das placas para sensação de movimento
y1 = -20  # posição inicial da peça entre pistas
y2 = -50  # posição inicial da placa
numplaca = randint(0, 3)     # escolha da placa a ser mostrada de forma randômica

# carro do jogador
carro = pygame.image.load('imagens/carro-verde.png')
x = 390
y = 400
v = 10

# carro 1 (azul)
carro1 = pygame.image.load('imagens/carro-azul.png')
xc1 = 250
yc1 = -100
vc1 = -9

# carro 2 (branco)
carro2 = pygame.image.load('imagens/carro-branco.png')
xc2 = 390
yc2 = -550
vc2 = -10

# carro 3 (amarelo)
carro3 = pygame.image.load('imagens/carro-amarelo.png')
xc3 = 530
yc3 = -320
vc3 = -9

# contagem de tempo
fonte = pygame.font.SysFont('courier new', 30)
texto = fonte.render(' Tempo ', True, (255, 255, 255), (0, 0, 0))
texto1 = fonte.render(' 000 s ', True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (90, 40)
pos_texto1 = texto1.get_rect()
pos_texto1.center = (90, 74)
tempo = 0
tempo_segundos = 0

# colisão
fonte_colisao = pygame.font.SysFont('arial bold', 50)
texto_colisao = fonte_colisao.render(' CRASH!! ', True, (255, 0, 0), (0, 0, 0))
pos_texto_colisao = texto_colisao.get_rect()
pos_texto_colisao.center = (100, 200)
colisao = False

# game over
fonte_gameover = pygame.font.SysFont('arial bold', 60)
texto_gameover = fonte_gameover.render(' FIM DE JOGO! ', True, (255, 255, 0), (0, 0, 0))
pos_texto_gameover = texto_gameover.get_rect()
pos_texto_gameover.center = (430, 300)

# definição inicial do jogo
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jogo de Corrida')

# loop eterno para execução do jogo
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)  # delay para refresh da tela em milisegundos
    for event in pygame.event.get():  # avaliação de eventos
        if event.type == pygame.QUIT:  # avaliação do evento de saída da janela (click no X)
            janela_aberta = False

    # comandos de controle do carrinho
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] and y > 5:
        y -= v
    if comandos[pygame.K_DOWN] and y < 450:
        y += v
    if comandos[pygame.K_RIGHT] and x < 560:
        x += v
    if comandos[pygame.K_LEFT] and x > 220:
        x -= v

    # mostrando fundo, entrefaixas e placa de trânsito
    janela.blit(fundo, (0, 0))  # mostra fundo no canto superior esquerdo (0,0)
    janela.blit(entrefaixas, (340, y1))
    janela.blit(entrefaixas, (480, y1))
    janela.blit(placas[numplaca], (650, y2))
    janela.blit(texto, pos_texto)

    # incrementando contagem do tempo
    if tempo < 20:
        tempo += 1
    else:
        tempo_segundos += 1
        texto1 = fonte.render(f' {tempo_segundos:3} s ', True, (255, 255, 255), (0, 0, 0))
        tempo = 0

    janela.blit(texto1, pos_texto1)

    # carros 1, 2, 3
    janela.blit(carro1, (xc1, yc1))
    janela.blit(carro2, (xc2, yc2))
    janela.blit(carro3, (xc3, yc3))

    # movimentação da placa e das faixas para gerar efeito de movimento
    y1 -= v1
    y2 -= v1
    if y1 > 610:
        y1 = -20
    if y2 > 610:
        y2 = -50
        numplaca = randint(0, 3)     # escolha da placa a ser mostrada de forma randômica

    # movimentação do carro 1
    yc1 -= vc1
    if yc1 > 710:
        yc1 = randint(-300, -100)

    # movimentação do carro 2
    yc2 -= vc2
    if yc2 > 760:
        yc2 = randint(-800, -600)

    # movimentação do carro 3
    yc3 -= vc3
    if yc3 > 800:
        yc3 = randint(-550, -350)

    # colisão com carro da direita
    if (x + 60 > xc3) and (y + 140 > yc3) and (y < yc3 + 120):
        colisao = True

    # colisão com carro da esquerda
    if (x - 60 < xc1) and (y + 140 > yc1) and (y < yc1 + 120):
        colisao = True

    # colisão com carro central
    if (x - 60 < xc2) and (x + 60 > xc2) and (y + 140 > yc2) and (y < yc2 + 120):
        colisao = True

    if colisao:
        janela.blit(texto_colisao, pos_texto_colisao)
        janela.blit(texto_gameover, pos_texto_gameover)

    janela.blit(carro, (x, y))  # carrinho controlado pelo usuário (verde)

    pygame.display.update()  # atualiza a tela

    if colisao:
        pygame.time.delay(2000)  # delay para refresh da tela em milisegundos
        colisao = False
        x = 390
        y = 400
        xc1 = 250
        yc1 = -100
        xc2 = 390
        yc2 = -550
        xc3 = 530
        yc3 = -320
        tempo = 0
        tempo_segundos = 0

pygame.quit()
