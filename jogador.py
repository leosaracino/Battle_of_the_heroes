from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from PPlay.animation import *
def set_animation(direita,esquerda,parado,jogador):
    for i in jogador:
        jogador[i].hide() 
    if direita:
        jogador['direita'].unhide()
    elif esquerda:
        jogador['esquerda'].unhide()
    else:
        jogador['parado'].unhide()

class Jogador():    

    @classmethod
    def controles(self,jogador, janela, velX, velY, teclado, jump, a, b, c, d):

        posInicial = jogador['direita'].x
        last = ''
        ##Física do pulo
        if jogador['direita'].y > janela.height - jogador['direita'].height - 30:

            jump = True  

        else:
            for i in jogador:
                jogador[i].y -= velY * janela.delta_time()   
            velY-= 1600 * janela.delta_time()

        ##Controles
        if teclado.key_pressed(a):

            if(jump):

                velY = 1000
                for i in jogador:
                    jogador[i].y -= velY * janela.delta_time()

            jump = False

        if teclado.key_pressed(b):

            velY-= 1600 * janela.delta_time()
        if teclado.key_pressed(c) and jogador['direita'].x > 0:
            last = 'direita'

            for i in jogador:
                jogador[i].x -= velX * janela.delta_time()

            set_animation(0,1,0,jogador)
        if teclado.key_pressed(d) and jogador['direita'].x < janela.width - jogador['direita'].width:
            last = 'esquerda'

            for i in jogador:
                jogador[i].x += velX * janela.delta_time()

            set_animation(1,0,0,jogador)

        if jogador['direita'].x == posInicial:

            set_animation(0,0,1,jogador)

        return velY , jump