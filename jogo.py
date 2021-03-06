# from Assets.torcida2.jpg import torcida2.jpg 
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from jogador import *
from PPlay.animation import *

class Jogo():
    def init():
        cont = 0
        fps = 0
        atual = 0
        rounds = 1
        contround1 = 0
        contround2 =0
        janela = Window(1280,720)
        janela.set_title("Battle of the heroes")
        janela.update()
        teclado = Window.get_keyboard()
        seg = janela.time_elapsed()
        fundoVitoria1 = GameImage("Assets/Player 1 wins.png")
        fundoVitoria2 = GameImage("Assets/Player 2 wins.png")
        while rounds <= 3:
            sprites1 = {'direita' : Sprite("Assets/Jogador1/Corrida-direita.png", 8), 'esquerda' :Sprite("Assets/Jogador1/Corrida-esquerda.png", 8), 'parado-direita' :Sprite("Assets/Jogador1/parado-direita.png",5),'parado-esquerda': Sprite("Assets/Jogador1/parado-esquerda.png",5), 'ataque-direita' :Sprite("Assets/Jogador1/Ataque-direita.png", 7), 'ataque-esquerda' :Sprite("Assets/Jogador1/ataque-esquerda.png", 7)}
            for i in sprites1:
                sprites1[i].set_position(20,janela.height - sprites1[i].height - 30)
                if i != 'ataque-direita' and i != 'ataque-esquerda':
                    sprites1[i].set_total_duration(1000)
                else:
                    sprites1[i].set_total_duration(300)
            
            sprites2 = {'direita' : Sprite("Assets/Jogador2/Corrida-direita.png", 8), 'esquerda' :Sprite("Assets/Jogador2/Corrida-esquerda.png", 8), 'parado-direita' :Sprite("Assets/Jogador2/parado-direita.png",5),'parado-esquerda': Sprite("Assets/Jogador2/parado-esquerda.png",5), 'ataque-direita' :Sprite("Assets/Jogador2/Ataque-direita.png", 7), 'ataque-esquerda' :Sprite("Assets/Jogador2/Ataque-esquerda.png", 7)}
            for i in sprites2:
                sprites2[i].set_position(janela.width-sprites2[i].width-20,janela.height - sprites2[i].height - 30)
                if i != 'ataque-direita' and i != 'ataque-esquerda':
                    sprites2[i].set_total_duration(1000)
                else:
                    sprites2[i].set_total_duration(300)

            pe = Sprite("Assets/pe_jogador.png", 1)
            pe2 = Sprite("Assets/pe_jogador.png", 1)
            pe.set_position(66,janela.height - pe.height - 33)
            pe2.set_position(janela.width-pe.width-66,janela.height - pe.height - 33)

            fundo = GameImage("Assets/fundo.png")


            plataformas= [GameImage("Assets/chao-plataformaPequena.png"),GameImage("Assets/chao-plataformaMedia.png"),GameImage("Assets/chao-plataformaPequena.png")]
            plataformas[0].set_position(146,janela.height - 257)
            plataformas[1].set_position(436,janela.height - 411)
            plataformas[2].set_position(janela.width - 320, janela.height - 257)
            jogador1 = Jogador(sprites1,450,0,True,"w","s","a","d","space")
            jogador2 = Jogador(sprites2,450,0,True,"up","down","left","right","enter")
            while True:
                ##FPS
                cont += janela.delta_time()
                fps += 1
                if cont>1:
                    atual= fps
                    cont=0
                    fps=0
                if rounds >= 1:
                    while janela.time_elapsed() - seg < 2500:
                        fundo.draw()
                        janela.draw_text(f"Round {rounds}", 436, 200, size=100, color=(0,0,0), font_name= 'Segoe UI', bold=True, italic=False)
                        janela.update()
                        
                ##Atualizaçao jogadores
                jogador1.controles( janela, teclado, plataformas, pe)
                jogador2.controles( janela, teclado, plataformas, pe2)

                if jogador1.attacking:
                    if jogador1.sprites[jogador1.getcurr_animation()].collided(jogador2.sprites[jogador2.getcurr_animation()]):
                        jogador2.take_damange()
                else:
                    jogador2.invulnerable = False
                
                if jogador2.attacking:
                    if jogador2.sprites[jogador2.getcurr_animation()].collided(jogador1.sprites[jogador1.getcurr_animation()]):
                        jogador1.take_damange()
                else:
                    jogador1.invulnerable = False
                ##Draws
                fundo.draw()
                janela.draw_text(f"FPS:{atual}", 10, 10, size=25, color=(255,255,255), font_name= 'Segoe UI', bold=False, italic=False)
                if jogador2.life == 0:
                    contround1 +=1
                    if contround1 == 2:
                        seg = janela.time_elapsed()
                        while janela.time_elapsed() - seg < 2500:
                            fundoVitoria1.draw()
                            janela.update()
                        rounds = 4
                        break
                    else:
                        seg = janela.time_elapsed()
                        rounds+=1
                        break
                if jogador1.life == 0:
                    contround2 +=1
                    if contround2 == 2:
                        seg = janela.time_elapsed()
                        while janela.time_elapsed() - seg < 2500:
                            fundoVitoria2.draw()
                            janela.update()
                        rounds = 4
                        break
                    else:
                        seg = janela.time_elapsed()
                        rounds+=1
                        break
                jogador1.draw()
                jogador2.draw()
                janela.update()
