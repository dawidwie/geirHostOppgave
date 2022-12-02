import pygame, sys, random, mysql.connector, tkinter, tkinter.simpledialog, time
from pygame.locals import *

# Displays dialouge box that gets player name
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
    
    #Sends information to database if score is higher than 0
    if result > 0:

        sequel= "insert into playerScore(player,score) values(%s, %s)"
        val = (playername.strip(), result)
        mycursor.execute(sequel,val)
        my.commit()

    #fetches highscore list sorted by score
    mycursor.execute("select * from playerScore order by score desc")   
    scores = mycursor.fetchmany(size=10)
    window.fill(black)

    #Displays player score
    scoredis = font.render("Y o u r   S c o r e",True,white)
    scoredisrect = scoredis.get_rect()
    scoredisrect.center = (window_width //2, window_height // 2)
    scoredisrect.top = 70
    scoreshow = bigfont.render(str(result), True, white)
    scoreshowrect = scoreshow.get_rect()
    scoreshowrect.center = (window_width //2, window_height // 2)
    scoreshowrect.top = 150
    continuetxt = enterfont.render("P R E S S   S P A C E   T O   C O N T I N U E",True,white)
    continuetxtrect = continuetxt.get_rect()
    continuetxtrect.left = 20
    continuetxtrect.bottom = 490
    window.blit(scoredis,scoredisrect)
    window.blit(scoreshow,scoreshowrect)
    pygame.display.update()
    time.sleep(0.2)
    window.blit(continuetxt,continuetxtrect)
    pygame.display.update()

    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            break


    #sets top height value and displays "TOP 10 HIGH SCORES" to game
    window.fill(black)
    topval = 70
    toplist = 1
    highscore = highfont.render("T O P   1 0   H I G H   S C O R E S",True,white)
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
        
        topval += 35
        toplist += 1
    pygame.display.update()
    enterwait = enterfont.render("P R E S S   E N T E R   T O   S T A R T   N E W   G A M E ", True, white)
    enterwaitrect = enterwait.get_rect()

    enterwaitrect.right = 375
    enterwaitrect.bottom = 490
    time.sleep(0.2)
    window.blit(enterwait,enterwaitrect)
    pygame.display.update()

    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_RETURN:
            break
                
            


    
    


#setting up variables
window_width = 600
window_height = 500
window = pygame.display.set_mode((window_width,window_height))
fps = 32
pipeimg = 'images/pipeleo.jpg'
backgroundimg = 'images/background.jpg'
leoimg = 'images/leo.jpg'
seaimg = 'images/base.jfif'
explosion = 'images/explosion2.png'
explosion_sound = 'sounds/explosionSoun.mp3'
leo_sound = 'sounds/leoSoun.mp3'
gameimgs = {}
elevation = window_height * 0.8
player_score = 0
white = (255,255,255)
black = (0,0,0)
green = (163,252,84)


def flappygame():
    #reset player score
    global player_score
    player_score = 0

    #set area and leo variables
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

    #set variables for pipes and leo
    pipeVelx = -4
    leo_velocity_y = -9
    leo_max_vel_y = 10
    leo_min_vel_y = -8
    leoAccY = 1
    leo_flap_vel = -8
    leo_flap = False


    while True:
        #checks for user input
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP) or event.type == MOUSEBUTTONDOWN:
                if vertical > 0:
                    leo_velocity_y = leo_flap_vel
                    leo_flap = True
                    pygame.mixer.Sound.play(jump)
                    pygame.mixer.music.stop()

        #checks if player collisions happens
        gameover = GameOver(horizontal, vertical, uppipes, downpipes)
        if gameover:
            window.blit(gameimgs['explosion'],(horizontal-25, vertical-15))
            pygame.display.update()
            pygame.mixer.Sound.play(crash)
            pygame.mixer.music.stop()
            sql()
            return

        #Checks if player has passed a pipe
        playerMidPos = horizontal + gameimgs['leo'].get_width()/2
        for pipe in uppipes:
            pipeMidPos = pipe['x'] + gameimgs['pipe'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos +4:
                player_score += 1

    
        if leo_velocity_y < leo_max_vel_y and not leo_flap:
            leo_velocity_y += leoAccY
        
        
        if leo_flap:
            leo_flap = False
        playerHeight = gameimgs['leo'].get_height()
        vertical = vertical + min(leo_velocity_y, elevation - vertical - playerHeight)


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

        #draw pipes, background and leo onto game
        window.blit(gameimgs['background'], (0,0))
        for upperPipe, lowerPipe in zip(uppipes, downpipes):
            window.blit(gameimgs['pipe'][0], (upperPipe['x'], upperPipe['y']))
            window.blit(gameimgs['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
        window.blit(gameimgs['sea_lvl'], (ground,elevation))
        window.blit(gameimgs['leo'], (horizontal, vertical))


        #Draw score to screen
        player_scoredis = highfont.render(str(player_score),True, white)
        player_scoredisrect = player_scoredis.get_rect()
        player_scoredisrect.top = 10
        player_scoredisrect.right = 570
        if player_score >= 10:
            player_scoredisrect.right = 568
        if player_score >= 100:
            player_scoredisrect.right = 566
        window.blit(player_scoredis,player_scoredisrect)

        #Update display at set frames per second
        pygame.display.update()
        fpsclock.tick(fps)

#creates pipe at random height
def createPipe():
    offset = window_height/3
    pipeheight = gameimgs['pipe'][0].get_height()
    pipeY2 = offset + random.randrange(0, int(window_height - gameimgs['sea_lvl'].get_height() -1.2*offset))
    pipeX = window_width + 10
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
        if (vertical < (pipeHeight + pipe['y']-2 ) and abs(horizontal - pipe['x']) < (gameimgs['pipe'][0].get_width()-5)):
            return True

        for pipe in down_pipes:
            if (vertical + gameimgs['leo'].get_height()-2 > (pipe['y'])) and abs(horizontal - pipe['x']) < (gameimgs['pipe'][0].get_width()-5):
                return True
        
        return False



#Game starts here
if __name__ == "__main__":
    
    #initializes pygame modules
    pygame.init()
    pygame.mixer.init()
    fpsclock = pygame.time.Clock()

    smallfont = pygame.font.Font('ARCADECLASSIC.TTF', 15)
    font = pygame.font.Font('ARCADECLASSIC.TTF', 28)
    highfont = pygame.font.Font('ARCADECLASSIC.TTF', 40)
    enterfont = pygame.font.Font('ARCADECLASSIC.TTF', 20)
    bigfont = pygame.font.Font('ARCADECLASSIC.TTF', 60)

    #sets name for game window
    pygame.display.set_caption('Flappy Leo Game')

    #Loads game images and sound
    gameimgs['pipe'] = (pygame.transform.rotate(pygame.image.load(pipeimg).convert_alpha(),180), pygame.image.load(pipeimg).convert_alpha())
    gameimgs['background'] = pygame.image.load(backgroundimg).convert_alpha()
    gameimgs['sea_lvl'] = pygame.image.load(seaimg).convert_alpha()
    gameimgs['leo'] = pygame.image.load(leoimg).convert_alpha()
    gameimgs['explosion'] = pygame.image.load(explosion).convert_alpha()
    jump = pygame.mixer.Sound(leo_sound)
    crash = pygame.mixer.Sound(explosion_sound)

    #Start screen for first game
    window.fill(black)
    start = bigfont.render("F L A P P Y   L E O",True, green)
    startrect = start.get_rect()
    startrect.center = (window_width // 2, window_height // 2)
    startrect.top = 125
    space = font.render("P R E S S   S P A C E   T O   S T A R T",True,white)
    spacerect = space.get_rect()
    spacerect.center = (window_width // 2, window_height // 2)
    spacerect.top = 250
    window.blit(start,startrect) 
    pygame.display.update()
    time.sleep(0.5)
    window.blit(space,spacerect)
    pygame.display.update()

    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:    
                break
    
    pygame.event.clear()
    while True:
        #sets variables for collision and leo placement
        vertical = (window_height - gameimgs['leo'].get_height())/2
        horizontal = window_width/5
        ground = 0

        #Checks for user input and starts game if right input
        while True:
            for event in pygame.event.get(): 
                
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP) or event.type == MOUSEBUTTONDOWN:
                    flappygame()

                else:
                    window.blit(gameimgs['background'], (0,0))
                    window.blit(gameimgs['leo'], (horizontal, vertical))
                    window.blit(gameimgs['sea_lvl'],(ground, elevation))

                    pygame.display.update()

                    fpsclock.tick(fps) 
