#coding: utf-8
# ------- Código do jogo "UFCG: The Journey -------------#
# Este arquivo contém os níveis e o que detecta que os   #
# comandos do teclado.                                   #
#     Ana Ribeiro e Matteus Silva, fevereiro de 2015     #   
import pygame, sys, time, personagem


class Nivel1():
    bg_num = 1
    bg1 = "img/sayonara.png"

def jogar():
    window = pygame.display.set_mode((800, 600)) 
    pygame.init()
    nivel = Nivel1()
    player = personagem.Personagem()
    pygame.init()
    fundo = pygame.image.load(nivel.bg1)
    
    #O segundo parâmetro da função define o delay das teclas.
    pygame.key.set_repeat(10, 20) 
    
    window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
    window.blit(fundo, (0, 0))
    
    # botao que define a pausa (por enquanto voltando para o menu)
    pausa = False
    
    while True:
        pygame.mouse.set_visible(False)
        window.blit(player.walking_frames_r[0], (player.pos_x, player.pos_y))
        if pausa == True:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausa = True
                if event.key == pygame.K_LEFT:
                    if (player.pos_x != 0):
                        player.esquerda()
                if event.key == pygame.K_RIGHT:
                    if (player.pos_x != 800):
                        player.direita()
                    else:
                        player.pos_x = 0
                if event.key == pygame.K_UP:
                    player.cima()
                    
    
        pygame.display.update()

    
