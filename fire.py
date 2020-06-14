import pygame
import random,math
from pygame import mixer

def showscore(x,y):
    score=font.render("Score :"+str(scoreval),True,(0,255,0))
    screen.blit(score, (x,y))

def gameover():
    overtext=overfont.render("GAME OVER",True,(255,255,255))
    screen.blit(overtext,(200,250))    


def enemy(x,y,i):
    screen.blit(enemyimage[i],(x,y))

def player(x,y):
    screen.blit(playerimage,(x,y))

def firebullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimage,(x+16,y+10))

def isCollision(enemyx,enemyy,bulletx,bullety):
    distance= math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))
    if distance <27:
        return True
    else:
        return False    

def start1():
    global screen,font,playerimage,playerychange,overfont,bulletimage,bulletxchange,enemyimage,showscore,scoreval,enemyy,bulletx,bullety,enemyx,bulletychange,bulletxchange,bulletstate
    pygame.init()
    screen=pygame.display.set_mode((800,600))

    background =pygame.image.load('background1.png')
    mixer.music.load('background.wav')
    mixer.music.play(-1)
    pygame.display.set_caption("Space Invaders")
    icon=pygame.image.load('ufo.png')
    playerimage=pygame.image.load('player.png')
    playerx=370
    playery=480
    playerxchange=0
    playerychange=0
    scoreval=0
    font=pygame.font.Font('freesansbold.ttf',32)
    textx=10
    texty=10
    overfont=pygame.font.Font('freesansbold.ttf',64)
    enemyimage=[]
    enemyx=[]
    enemyy=[]
    enemyxchange=[]
    enemyychange=[]
    numofenemies=6

    for i in range(numofenemies):
        enemyimage.append(pygame.image.load('enemy.png'))
        enemyx.append(random.randint(0,736))
        enemyy.append(random.randint(50,150))
        enemyxchange.append(3.5)
        enemyychange.append(40)

    bulletimage=pygame.image.load('bullet.png')
    bulletx=0
    bullety=480
    bulletxchange=0
    bulletychange=14
    bulletstate="ready"

    pygame.display.set_icon(icon)

    running=True

    while running:
        screen.fill((0,0,0)) 
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type ==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:  
                    playerxchange=-12
                if event.key==pygame.K_RIGHT:
                    playerxchange=12
                if event.key==pygame.K_SPACE:   

                    if bulletstate is "ready": 
                        # bullet_sound=mixer.Sound('laser.wav')
                        # bullet_sound.play()
                        bulletx=playerx         
                        firebullet(bulletx,bullety)
            if event.type==pygame.KEYUP:
                    playerxchange=0

        playerx=playerx+playerxchange    
        if playerx <=0:
            playerx=0
        elif playerx >=736:
            playerx=736

        for i in range(numofenemies):
            if enemyy[i]>440:
                for j in range(numofenemies):
                    enemyy[j]=2000
                gameover()
                break
            enemyx[i]+=enemyxchange[i]
            if enemyx[i]>=736:
                enemyxchange[i]=-3.5
                enemyy[i]=enemyy[i]+enemyychange[i]
            elif enemyx[i]<=0:
                enemyxchange[i]=3.5
                enemyy[i]=enemyy[i]+enemyychange[i]

            collision=isCollision(enemyx[i],enemyy[i],bulletx,bullety)
            if collision:
                # explosionsound=mixer.sound('explosion.wav')
                # explosionsound.play()
                bullety=480
                bulletstate="ready"
                scoreval+=1
                enemyx[i]=random.randint(0,736)
                enemyy[i]=random.randint(50,150)     

            enemy(enemyx[i],enemyy[i],i)

        if bullety<=0:
            bullety=480
            bulletstate="ready"

        if bulletstate is "fire":
            firebullet(bulletx,bullety)
            bullety=bullety-bulletychange

        player(playerx,playery)  
        showscore(textx,texty)
        pygame.display.update()


if __name__ == "__main__":
      start1()