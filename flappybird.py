import pygame, sys, random, mysql.connector, tkinter, tkinter.simpledialog, time
from pygame.locals import *

# Displays dialouge boc that gets player name
def getPlayerName() -> str:
    tk = tkinter.Tk()
    tk.withdraw()
    playerName = tkinter.simpledialog.askstring("Name?", "Enter name of player", parent=tk)
    tk.destroy()
    if playerName is None:
        playerName = "ANONYMOUS"
    return playerName

def sql():
    #Connects to database
    my = mysql.connector.connect(host="localhost", user="root", password="password", database="flappybird")
    mycursor = my.cursor()

    #sets score and name value
    result = int(player_score)
    playername = getPlayerName()
    
        
    #Sends information
    sequel= "insert into playerScore(player,score) values(%s, %s)"
    val = (playername, result)
    mycursor.execute(sequel,val)
    my.commit()

    #fetches highscore list sorted by score
    mycursor.execute("select * from playerScore order by score desc")   
    scores = mycursor.fetchmany(size=10)

    #sets font and size for highscore list
    font = pygame.font.Font('ARCADECLASSIC.TTF', 28)
    highfont = pygame.font.Font('ARCADECLASSIC.TTF', 40)
    enterfont = pygame.font.Font('ARCADECLASSIC.TTF', 20)


    #sets top height value and displays "TOP 10 HIGH SCORES" to game
    window.fill(black)
    topval = 70
    toplist = 1
    highscore = highfont.render("TOP  10  HIGH  SCORES",True,white)
    highscorerect = highscore.get_rect()
    highscorerect.center = (window_width // 2, window_height // 2)
    highscorerect.top = 10
    window.blit(highscore,highscorerect)

    #Displays top 10 scores
    for row in scores:
        scorekey = row[1].strip()
        scoreval = row[2]
        scoreIn = f"{str(toplist)}  {scorekey}  {scoreval}"
        text = font.render(scoreIn,True,white)
        textrect= text.get_rect()
        textrect.center = (window_width // 2, window_height // 2)
        textrect.top = topval
        window.blit(text,textrect)
        print(scoreIn)
        pygame.display.update()
        topval += 35
        toplist += 1
    
    enterwait = enterfont.render("P R E S S   E N T E R   T O   S T A R T   N E W   G A M E ", True, white)
    enterwaitrect = enterwait.get_rect()

    enterwaitrect.right = 375
    enterwaitrect.bottom = 490
    window.blit(enterwait,enterwaitrect)
    pygame.display.update()

    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                return
                
            


    
    


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
player_score = 0
white = (255,255,255)
black = (0,0,0)

def flappygame():
    #reset player score
    global player_score
    player_score = 0

    #set area variables
    horizontal = window_height/5
    vertical = window_width/2
    ground = 0
    tempheight = 100

    #create first obstacle
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

    #set variables for pipes and bird
    pipeVelx = -4
    bird_velocity_y = -9
    bird_max_vel_y = 10
    bird_min_vel_y = -8
    birdAccY = 1
    bird_flap_vel = -8
    bird_flap = False


    while True:
        #checks for user input
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if vertical > 0:
                    bird_velocity_y = bird_flap_vel
                    bird_flap = True
        
        #checks if player collisions happens
        gameover = GameOver(horizontal, vertical, uppipes, downpipes)
        if gameover:
            sql()
            # time.sleep(3)
            return

        #Checks if player has passed a pipe
        playerMidPos = horizontal + gameimgs['bird'].get_width()/2
        for pipe in uppipes:
            pipeMidPos = pipe['x'] + gameimgs['pipe'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos +4:
                player_score += 1

    
        if bird_velocity_y < bird_max_vel_y and not bird_flap:
            bird_velocity_y += birdAccY
        
        
        if bird_flap:
            bird_flap = False
        playerHeight = gameimgs['bird'].get_height()
        vertical = vertical + min(bird_velocity_y, elevation - vertical - playerHeight)


        for upperPipe, lowerPipe in zip(uppipes, downpipes):
            upperPipe['x'] += pipeVelx
            lowerPipe['x'] += pipeVelx

        #Create new pipe if pipe count is under 5
        if 0 < uppipes[0]['x'] < 5:
            newpipe = createPipe()
            uppipes.append(newpipe[0])
            downpipes.append(newpipe[1])

        #deletes pipe if pipe goes out of range
        if uppipes[0]['x'] < -gameimgs['pipe'][0].get_width():
            uppipes.pop(0)
            downpipes.pop(0)

        #draw pipes, background and bird onto game
        window.blit(gameimgs['background'], (0,0))
        for upperPipe, lowerPipe in zip(uppipes, downpipes):
            window.blit(gameimgs['pipe'][0], (upperPipe['x'], upperPipe['y']))
            window.blit(gameimgs['pipe'][1], (lowerPipe['x'], lowerPipe['y']))


        window.blit(gameimgs['sea_lvl'], (ground,elevation))
        window.blit(gameimgs['bird'], (horizontal, vertical))

        #draw score onto screen
        numbers = [int(x) for x in list(str(player_score))]
        width = 0
        for num in numbers:
            width += gameimgs['scoreimgs'][num].get_width()
        Xoffset = (window_width-width)/1.1
        for num in numbers:
            window.blit(gameimgs['scoreimgs'][num], (Xoffset, window_width*0.03))
            Xoffset += gameimgs['scoreimgs'][num].get_width()

        #Update display at 32 frames per second
        pygame.display.update()
        fpsclock.tick(fps)

#creates pipe at random height
def createPipe():
    offset = window_height/3
    pipeheight = gameimgs['pipe'][0].get_height()
    pipeY2 = offset + random.randrange(0, int(window_height - gameimgs['sea_lvl'].get_height() -1.2*offset))
    pipeX = window_height + 10
    pipeY1 = pipeheight - pipeY2 + offset
    pipe = [
        #upper pipe
        {'x' : pipeX, 'y': -pipeY1},

        #lower pipe
        {'x': pipeX, 'y': pipeY2}
    ]
    return pipe

#checks for collision and returns True if true
def GameOver(horizontal, vertical, up_pipes, down_pipes):
    if vertical > elevation-25 or vertical < 0:
        return True
    
    for pipe in up_pipes:
        pipeHeight = gameimgs['pipe'][0].get_height()
        if (vertical < (pipeHeight + pipe['y'] -15 ) and abs(horizontal - pipe['x']) < (gameimgs['pipe'][0].get_width()-30)):
            return True

        for pipe in down_pipes:
            if (vertical + gameimgs['bird'].get_height() > (pipe['y'] +15)) and abs(horizontal - pipe['x']) < (gameimgs['pipe'][0].get_width()-30):
                return True
        
        return False



#Game starts here
if __name__ == "__main__":
    
    #initializes pygame modules
    pygame.init()
    fpsclock = pygame.time.Clock()

    #sets name for game window
    pygame.display.set_caption('Flappy Bird Game')

    #Load all images
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
        #sets variables for collision
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
