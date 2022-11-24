import pygame, sys, random, mysql.connector
from pygame.locals import *

def sql():
    #Connects to database
    my = mysql.connector.connect(host="localhost", user="root", password="password", database="flappybird")
    mycursor = my.cursor()
    result = 0 
    player = input("Enter your name: ")
    #Sends information
    mycursor.execute("insert into table(player,score) values ({}, '{}')".format(player,result))
    mycursor.commit()

#setting up variables
window_width = 600
window_height = 500
window = pygame.display.set_mode((window_width,window_height))
fps = 32
pipeimg = 'images/pipe.png'
backgroundimg = 'images/background.jpg'
birdimg = 'images/bird.png'
seaimg = 'images/base.jfif'
gameimgs = {}
elevation = window_height * 0.8

def createPipe():
    offset = window_height/3
    pipeheight = gameimgs['pipe'][0].get_height()

    pipeY2 = offset + random.randrange(0, window_height - gameimgs['sea_lvl'].get_height() -1.2*offset)
    pipeX = window_height + 10
    pipeY1 = pipeheight - pipeY2 + offset
    pipe = [
        #upper pipe
        {'x' : pipeX, 'y': -pipeY1},

        #lower pipe
        {'x': pipeX, 'y': pipeY2}
    ]
    return pipe

def GameOver(horizontal, vertical, up_pipes, down_pipes):
    if vertical > elevation -25 or vertical < 0:
        return True
    
    for pipe in up_pipes:
        pipeHeight = gameimgs['pipe'][0].get_height()
        if (vertical < pipeHeight + pipe['y'] and abs(horizontal - pipe['x']) < gameimgs['pipe'][0].get_width()):
            return True

        for pipe in down_pipes:
            if (vertical + gameimgs['bird'].get_height() > pipe['y']) and abs(horizontal - pipe['x']) < gameimgs['pipe'][0].get_width():
                return True
        
        return False

def flappygame():
    player_score = 0
    horizontal = window_height/5
    vertical = window_width/2
    ground = 0
    tempheight = 100

    firstpipe = createPipe()
    secondpipe = createPipe()

    downpipes = [
        {'x' : window_width+300-tempheight, 'y': firstpipe[1]['y']},
        {'x' : window_width+300-tempheight+(window_width/2),'y': secondpipe[1]['y']}
    ]
    
    uppipes = [
        {'x' : window_width+300-tempheight, 'y': firstpipe[0]['y']},
        {'x' : window_width+200-tempheight+(window_width/2),'y': secondpipe[0]['y']}       
    ]

    pipeVelx = -4
    bird_velocity_y = -9
    bird_max_vel_y = 10
    bird_min_vel_y = -8
    birdAccY = 1

    bird_flap_vel = -8

    bird_flap = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if vertical > 0:
                    bird_velocity_y = bird_flap_vel
                    bird_flap = True
        
        gameover = GameOver(horizontal, vertical, uppipes, downpipes)
        if gameover:
            return

        playerMidPos = horizontal + gameimgs['pipe'][0].get_width()/2
        for pipe in uppipes:
            pipeMidPos = pipe['y'] + gameimgs['pipe'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos +4:
                player_score += 1
                print(f"Your score is {player_score}")

        if bird_velocity_y < bird_max_vel_y and not bird_flap:
            bird_velocity_y += birdAccY
        
        if bird_flap:
            bird_flap = False
        playerHeight = gameimgs['bird'].get_height()
        vertical = vertical + min(bird_velocity_y, elevation - vertical - playerHeight)

        for upperPipe, lowerPipe in zip(uppipes, downpipes):
            upperPipe['x'] += pipeVelx
            lowerPipe['x'] += pipeVelx

        
        if 0 < uppipes[0]['x'] < 5:
            newpipe = createPipe()
            uppipes.append(newpipe[0])
            downpipes.append(newpipe[1])
        
        if uppipes[0]['x'] < -gameimgs['pipe'][0].get_width():
            uppipes.pop(0)
            downpipes.pop(0)

        window.blit(gameimgs['background'], (0,0))
        for upperPipe, lowerPipe in zip(uppipes, downpipes):
            window.blit(gameimgs['pipe'][0], (upperPipe['x'], upperPipe['y']))
            window.blit(gameimgs['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        window.blit(gameimgs['sea_lvl'], (ground,elevation))
        window.blit(gameimgs['bird'], (horizontal, vertical))

        numbers = [int(x) for x in list(str(player_score))]
        width = 0

        for num in numbers:
            width += gameimgs['scoreimgs'][num].get_width()
        Xoffset = (window_width-width)/1.1


        for num in numbers:
            window.blit(gameimgs['scoreimgs'][num], (Xoffset, window_width*0.03))
            Xoffset += gameimgs['scoreimgs'][num].get_width()

#Game starts here
if __name__ == "__main__":
    
    #initializes pygame modules
    pygame.init()
    fpsclock = pygame.time.Clock()

    pygame.display.set_caption('Flappy Bird Game')

    gameimgs['scoreimgs'] = (
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha()
    )
    gameimgs['pipe'] = (pygame.transform.rotate(pygame.image.load(pipeimg).convert_alpha(),180), pygame.image.load(pipeimg).convert_alpha())
    gameimgs['background'] = pygame.image.load(backgroundimg).convert_alpha()
    gameimgs['sea_lvl'] = pygame.image.load(seaimg).convert_alpha()
    gameimgs['bird'] = pygame.image.load(birdimg).convert_alpha()

    print("WELCOME TO FLAPPY BIRD")
    print("Press space or enter to start")

    while True:

        vertical = (window_height - gameimgs['bird'].get_height())/2
        horizontal = window_width/5
        
        ground = 0

        while True:
            for event in pygame.event.get(): 
                
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    flappygame()

                else:
                    window.blit(gameimgs['background'], (0,0))
                    window.blit(gameimgs['bird'], (horizontal, vertical))
                    window.blit(gameimgs['sea_lvl'],(ground, elevation))

                    pygame.display.update()

                    fpsclock.tick(fps)
