#colocar musica 
#colocar efeito sonoro
#botão de restart 
#deixar a velocidade maior quando pegar 3, 5, 10 

import pygame
import random #permite pegar numero aleatoria dentro de range ou lista #gera algo aleatoria na tela

#Inicia o pygame e a musica 
pygame.init()
pygame.mixer.init()

#carregar musica para o jogo
pygame.mixer.music.load(r"C:\HitPaw Video Converter\Downloaded.mp3") ##COLOCAR O AQUIVO DA MUSICA 

#Ajusta volume da musica
pygame.mixer.music.set_volume(0.7)

#Colocar para tocar
pygame.mixer.music.play(-1) #"0" toca uma vez e "-1" toca infinito 

#mantem programa rodando enquanto a musica toca 
while pygame.mixer.music.play.get_busy():
    pygame.time.Clock().tick(10) #atualiza a cada 10ms para evitar congelamento 

pygame.display.set_caption("Jogo da cobrinha")
LARGURA, ALTURA = 1200, 800
tela =pygame.display.set_mode((LARGURA, ALTURA))

relogio = pygame.time.Clock()

#Cores RGB
preta = (0,0,0)
branca= (255,255,255)
vermelha = (255,0,0)
verde= (0,255,0)

tamanho_quadrado= 20 #sempre numero par e inteiro

#FPS do jogo 
velocidade_jogo= 5

#Gerar a comida inicial
comida_x= round(random.randrange(0,LARGURA - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
comida_y= round(random.randrange(0,ALTURA - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

#Posição inicial da cabeça da cobra 
x = LARGURA/2
y = ALTURA/2

velocidade_x = 0
velocidade_y = 0

#Compriemto inicial da cobra
tamanho_cobra = 1
#Corpo da cobra
segmentos_cobra= [] 

fim_jogo = False
fim_jogo = pygame.mixer.music.stop() ###Analisarr

while not fim_jogo:
    #Criando a tela do jogo 
    tela.fill(preta) 

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                velocidade_x = 0
                velocidade_y = tamanho_quadrado
            elif evento.key == pygame.K_UP:
                velocidade_x = 0
                velocidade_y = -tamanho_quadrado
            elif evento.key == pygame.K_RIGHT:
                velocidade_x = tamanho_quadrado
                velocidade_y = 0
            elif evento.key == pygame.K_LEFT:
                velocidade_x = -tamanho_quadrado
                velocidade_y = 0
            

    #Atualizar a posição da cobrinha
    x += velocidade_x
    y += velocidade_y

    #Atualizar o corpo da cobrinha
    segmentos_cobra.append([x,y])
    if len(segmentos_cobra) > tamanho_cobra:
        del segmentos_cobra[0]
    
    #verificar colisão com o prorpio corpo
    for lista in segmentos_cobra[:-1]:
        if lista == [x,y]:
            fim_jogo = True and pygame.mixer.music.stop()
            
    
    #verificar  colisão na parede
    if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
        fim_jogo = True and pygame.mixer.music.stop()
        
   
    #Desenhar a cobrinha
    for lista in segmentos_cobra:
        pygame.draw.rect(tela, verde, [lista[0], lista[1], tamanho_quadrado, tamanho_quadrado])

    #Desenhar a comida
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho_quadrado, tamanho_quadrado])

    #Desenho a pontuação 
    fonte = pygame.font.SysFont("Arial Black", 32)
    texto = fonte.render(f"Pontos: {tamanho_cobra-1}", True, branca)
    tela.blit(texto, [1,1])
 
    pygame.display.update()

    #verificar se a cobtrinha comeu a comida 
    if x == comida_x and y == comida_y:
        tamanho_cobra += 1

        #Gerar a comida inicial
        comida_x= round(random.randrange(0,LARGURA - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
        comida_y= round(random.randrange(0,ALTURA - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    
    relogio.tick(velocidade_jogo) 

pygame.quit()