import pygame

pygame.init()

Tamanho_tela =(800, 800) 
tela = pygame.display.set_mode(Tamanho_tela)
pygame.display.set_caption("JOGO")

Tamanho_bola = 15
bola = pygame.Rect(100, 500, Tamanho_bola, Tamanho_bola)
Tamanho_jogador = 100
jogador = pygame.Rect(0, 750, Tamanho_jogador, 15)

qtde_bloco_linha = 8
qtde_linhas_blocos = 5
qtde_total_blocos =  qtde_bloco_linha * qtde_linhas_blocos

def criar_blocos(qtde_bloco_linha, qtde_linhas_blocos):
    altura_tela = Tamanho_tela[1]
    largura_tela = Tamanho_tela[0]
    distancia_entre_blocos = 5
    largura_bloco = largura_tela / 8 - distancia_entre_blocos
    altura_bloco = 15
    distancia_entre_linhas = altura_bloco + 10
    
    blocos = []
    for i in range(qtde_linhas_blocos):
        for i in range(qtde_bloco_linha):
            bloco = pygame.rect(i * (largura_bloco + distancia_entre_blocos))
            blocos.append(bloco)
    return blocos 

cores = {
    "branca":(255,255,255),
    "preta":(0,0,0),
    "amarela":(255,255,0),
    "azul":(0,0,255),
    "verde":(0,255)  
}       

fim_jogo = False
pontuacao = 0
movimento_bola = [7, -7]

def inicio_jg():
    tela.fill(cores["preta"])
    pygame.draw.rect(tela, cores["azul"], jogador)
    pygame.draw.rect(tela, cores["branca"], bola)
    
def blocoss(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["verde"], bloco)
        
        
def movimentar(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            if (jogador.x + Tamanho_jogador) < Tamanho_tela[0]:
                jogador.x = jogador.x + 5
            if evento.key == pygame.K_LEFT:
                if jogador.x > 0:
                    jogador.x = jogador.x - 5
                    
def movimentar_bola(bola):
    movimento =  movimento_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]
    
    if bola.x <= 0:
        movimento[0] = - movimento[0]
    if bola.y <= 0:
        movimento[1] = - movimento[1]
    if bola.x + Tamanho_bola >= Tamanho_tela[0]:
        movimento[0] = - movimento[0]
    if bola.y + Tamanho_bola >= Tamanho_tela[1]:
        movimento = None
        
    if jogador.collidepoint(bola.x, bola.y):
        blocos.remove(bloco)
        movimento[1] = - movimento[1]
    return movimento

def atualizar_pontos(pontuacao):
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f" Pontuação: {pontuacao}", 1,cores["amarela"])
    tela.blit(texto,(0, 780))
    if pontuacao >= qtde_total_blocos:
        return True
    else:
        return False
    
blocos = criar_blocos(qtde_bloco_linha, qtde_linhas_blocos)

while not fim_jogo:
    inicio_jg()
    blocoss(blocos)
    fim_jogo = atualizar_pontos(qtde_total_blocos - len(blocos))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True
            
    movimentar(evento)
    movimentar_bola = movimentar_bola(bola)

    if not movimentar_bola:
        fim_jogo = True
    pygame.time.wait(1)
    pygame.display.flip()
    
pygame.quit()