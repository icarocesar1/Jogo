# Está importando a biblioteca pygame
import pygame

# Esse código está inicializando a biblioteca pygame,caso ele não consiga inicializar, ele executa a exceção.
try:
    pygame.init()
except:
    print("o modulo pygame nao foi inicializado com sucesso")

# Essas duas variavéis definem o tamanho da tela
largura = 640
altura = 304

# Variavéis referentes ao inimigo
posicao_do_inimigo_x = 480
posicao_do_inimigo_y = 304 / 2
largura_do_inimigo = 40
altura_do_inimigo = 80
velocidade_do_inimigo_x = 0
velocidade_do_inimigo_y = 0

# variavéis referentes ao herói
posicao_do_heroi_x = 40
posicao_do_heroi_y = 304 / 2
largura_do_heroi = 40
altura_do_heroi = 70
velocidade_do_heroix = 0
velocidade_do_heroiy = 0

# Variavéis referente a bala do herói
posicao_da_bala_x = posicao_do_heroi_x
posicao_da_bala_y = posicao_do_heroi_y
velocidade_da_bala_x = 1.5
velocidade_da_bala_y = 0
bala = pygame.image.load('Archer.png')  # Carregando a imagem da bala
bala = pygame.transform.scale(bala, (30, 20))
ball = False

# variavéis referentes a bala do inimigo
posicao_da_bala_inimigo_x = posicao_do_heroi_x
posicao_da_bala_inimigo_y = posicao_do_heroi_y
velocidade_da_bala_inimigo_x = -1.5
velocidade_da_bala_inimigo_y = 0
bala_inimigo = pygame.image.load('mage-bullet-13x13.png')
bala_inimigo = pygame.transform.scale(bala_inimigo, (20, 20))  # Diminuir o tamanho da bala
ball_inimigo = False

# Criando a tela e botando o nome na tela do jogo
cenario1 = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Código Quântico')

# Botando a música de fundo no jogo
Variavel_musica = pygame.mixer.Sound('musicWAV (online-audio-converter.com).wav')
Variavel_musica.play()

# Carregando o cenário do jogo
Fundo_Do_Jogo = pygame.image.load('Fundo_Do_Jogo.png').convert()

# Carregando a imagem do herói e do inimigo
Heroi = pygame.image.load('Arqueiro.png')
Heroi = pygame.transform.scale(Heroi, (37, 50))  # Diminuir o tamanho da bala
Inimigo = pygame.image.load('inimigo.png')

# Som do tiro e da colisão
som_tiro_heroi = pygame.mixer.Sound('tiro_heroi.wav')
colisao = pygame.mixer.Sound('colisao.wav')
som_tiro_inimigo = pygame.mixer.Sound('tiro_inimigo.wav')

# Pontuação do jogo
pontos_heroi = 0
pontos_inimigo = 0

# while principal do jogo
jogo = True
while jogo:
    cenario1.blit(Fundo_Do_Jogo, (0, 0))  # Adicionar a imagem do cenario na tela

    # Lendo os eventos
    for event in pygame.event.get():
        # Processa os eventos

        # Sair do jogo
        if event.type == pygame.QUIT:
            jogo = False

        # Analisa se uma tecla foi apertada
        if event.type == pygame.KEYDOWN:

            # Analisa se a tecla S foi apertada.Se apertada, andará para baixo.
            if event.key == pygame.K_s:
                velocidade_do_heroiy = 0.5
                velocidade_do_heroix = 0

            # Analisa se a tecla w foi apertada.Se apertada, andará para cima
            if event.key == pygame.K_w:
                velocidade_do_heroiy = -0.5
                velocidade_do_heroix = 0

            # Analisa se a tecla para baixo foi apertada.Se for apertada, o inimigo andará para baixo
            if event.key == pygame.K_DOWN:
                velocidade_do_inimigo_y = 0.5
                velocidade_do_inimigo_x = 0
            # Analisa se a tecla de cima foi apertada.Se for apertada, o inimigo andará para cima
            if event.key == pygame.K_UP:
                velocidade_do_inimigo_y = -0.5
                velocidade_do_inimigo_x = 0
            # Analisa se a tecla espaço foi apertada.Se foi apertada, sairá o tiro do herói
            if event.key == pygame.K_SPACE:
                if ball == False:
                    som_tiro_heroi.play()
                    posicao_da_bala_x = posicao_do_heroi_x
                    posicao_da_bala_y = posicao_do_heroi_y
                    ball = True  # A bala ira aparecer na tela
            # Analisa se a tecla backspace foi apertada. Se foi apertada, saira o tiro do inimigo
            if event.key == pygame.K_BACKSPACE:
                if ball_inimigo == False:
                    som_tiro_heroi.play()
                    posicao_da_bala_inimigo_x = posicao_do_inimigo_x
                    posicao_da_bala_inimigo_y = posicao_do_inimigo_y
                    ball_inimigo = True

        # Analisa se uma tecla foi soltada.Se for soltada, os personagens pararão de andar
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                velocidade_do_heroiy = 0
                velocidade_do_heroix = 0
            if event.key == pygame.K_w:
                velocidade_do_heroiy = 0
                velocidade_do_heroix = 0
            if event.key == pygame.K_DOWN:
                velocidade_do_inimigo_y = 0
                velocidade_do_inimigo_x = 0
            if event.key == pygame.K_UP:
                velocidade_do_inimigo_y = 0
                velocidade_do_inimigo_x = 0

    # Adicionando a imagem dos personagens na tela
    cenario1.blit(Heroi, (posicao_do_heroi_x, posicao_do_heroi_y))
    cenario1.blit(Inimigo, (posicao_do_inimigo_x, posicao_do_inimigo_y))

    # Fazerá a imagem da bala aparecer e o processo de colisão
    if ball == True:
        cenario1.blit(bala, (posicao_da_bala_x, posicao_da_bala_y))  # Adicionando a imagem da bala na tela
        balaRect = bala.get_rect(topleft=(
        posicao_da_bala_x, posicao_da_bala_y))  # retorna o retangulo da imagem da bala, para analisar as colisoes
        InimigoRect = Inimigo.get_rect(topleft=(posicao_do_inimigo_x,
                                                posicao_do_inimigo_y))  # retorna o retangulo da imagem do inimigo, para analisar as colisoes

        # Se a bala colidiu com o inimigo
        if balaRect.colliderect(InimigoRect):
            colisao.play()  # Som da colisão
            ball = False  # Desparecimento da bala
            pontos_heroi += 1  # Pontuação do herói

        # se a bala ultrapassar o limite da tela, ela desaparece
        if posicao_da_bala_x >= largura:
            ball = False

    if ball_inimigo == True:
        cenario1.blit(bala_inimigo, (posicao_da_bala_inimigo_x, posicao_da_bala_inimigo_y))
        balaRect = bala_inimigo.get_rect(topleft=(posicao_da_bala_inimigo_x, posicao_da_bala_inimigo_y))
        HeroiRect = Heroi.get_rect(topleft=(posicao_do_heroi_x, posicao_do_heroi_y))
        if balaRect.colliderect(HeroiRect):
            colisao.play()
            ball_inimigo = False
            pontos_inimigo += 1
            print("pontos Inimigo", pontos_inimigo)

        if posicao_da_bala_inimigo_x <= 0:
            ball_inimigo = False

    # Os personagens e a bala irão se mover
    posicao_do_inimigo_x += velocidade_do_inimigo_x
    posicao_do_inimigo_y += velocidade_do_inimigo_y
    posicao_do_heroi_x += velocidade_do_heroix
    posicao_do_heroi_y += velocidade_do_heroiy
    posicao_da_bala_x += velocidade_da_bala_x
    posicao_da_bala_inimigo_x += velocidade_da_bala_inimigo_x

    # Personagens nao ultrapassam o limite da tela
    if posicao_do_heroi_y >= altura - altura_do_heroi:
        velocidade_do_heroiy = 0
        posicao_do_heroi_y = altura - altura_do_heroi
    if posicao_do_heroi_y <= 0:
        velocidade_do_heroiy = 0
        posicao_do_heroi_y = 0
    if posicao_do_inimigo_y >= altura - altura_do_inimigo:
        posicao_do_inimigo_y = altura - altura_do_inimigo
        velocidade_do_inimigo_y = 0
    if posicao_do_inimigo_y <= 0:
        posicao_do_inimigo_y = 0
        velocidade_do_inimigo_y = 0

    if pontos_heroi == 3 or pontos_inimigo == 3:
        jogo = False

    # aparecer a pontuacao na tela
    txt1 = ("pontos: " + str(pontos_heroi))  ##### armazena o texto
    txt2 = ("pontos: " + str(pontos_inimigo))  ##### armazena o texto
    pygame.font.init()  ##### inicia fonte
    fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
    fontesys = pygame.font.SysFont(fonte, 60)  ##### usa a fonte padrão
    pontos_do_heroi_text = fontesys.render(txt1, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
    pontos_do_inimigo_text = fontesys.render(txt2, 1, (255, 255, 255))  ##### renderiza o texto na cor desejada
    cenario1.blit(pontos_do_heroi_text, (0, 0))
    cenario1.blit(pontos_do_inimigo_text, (largura - 250, 0))

    pygame.display.update()

pygame.quit()
