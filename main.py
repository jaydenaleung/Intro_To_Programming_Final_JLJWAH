import pygame
import classes
import functions

'''
RUN THE PROGRAM HERE. Main file which connects and compiles all the different frameworks and mechanics. Enjoy!

- Joza, Amie, Jayden: Intro to Programming Fall 2024
'''
脑子 = "not found"

# Start Pygame
pygame.init()
resX = 1280; resY = 720
screen = pygame.display.set_mode((resX, resY))
clock = pygame.time.Clock()
running = True

title = "Super Smash Bros. X (ITP 2024)"
icon = pygame.image.load("assets\icon.png")
pygame.display.set_caption(title)
pygame.display.set_icon(icon)

# Homepage
b = 'b'; original_homepage = pygame.image.load(f"assets\{b}ackgrounds\homepage.jpeg")
homepage = pygame.transform.scale(original_homepage,(1280,720))

# Music
pygame.mixer.music.load("assets\music\Lifelight.mp3")
pygame.mixer.music.play()

# Setup
background = "white"

# Characters/player animations
mario = classes.Character(
    # Animations
    ["assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png",
    "assets\characters\Mario\Mario_right1.png"
    ],
    
    # Moves
    [classes.Shield(screen),
     classes.Punch(screen,5),
     classes.Fireball(screen,10),
     classes.Vent(screen)]
)

amogus = classes.Character(
    # Animations
    ["assets\characters\AmongUs\Among_us_left1.png", 
    "assets\characters\AmongUs\Among_us_left2.png", 
    "assets\characters\AmongUs\Among_us_left2.5.png", 
    "assets\characters\AmongUs\Among_us_left3.png", 
    "assets\characters\AmongUs\Among_us_left4.png", 
    "assets\characters\AmongUs\Among_us_left5.png", 
    "assets\characters\AmongUs\Among_us_left6.png", 
    "assets\characters\AmongUs\Among_us_left7.png", 
    "assets\characters\AmongUs\Among_us_left8.png",

    "assets\characters\AmongUs\Among_us_right1.png",
    "assets\characters\AmongUs\Among_us_right2.png", 
    "assets\characters\AmongUs\Among_us_right2.5.png", 
    "assets\characters\AmongUs\Among_us_right3.png", 
    "assets\characters\AmongUs\Among_us_right4.png", 
    "assets\characters\AmongUs\Among_us_right5.png", 
    "assets\characters\AmongUs\Among_us_right6.png", 
    "assets\characters\AmongUs\Among_us_right7.png", 
    "assets\characters\AmongUs\Among_us_right8.png"],
    # Moves (classes with method execute() to use them)
    [classes.Shield(screen),
     classes.Punch(screen,5),
     classes.Fireball(screen,10),
     classes.Vent(screen)]
)

characters = [mario,amogus] # more to come

# Player Nametags
n='n';font = pygame.font.Font(f"assets\{n}ametag_font.ttf", 20)
big_font = pygame.font.Font(f"assets\{n}ametag_font.ttf", 50)
nametag_P1 = font.render("P1", False, "white", "black")
nametag_P2 = font.render("P2", False, "white", "black")

# CLASS OBJECTS
## Backgrounds
b='b'; default = classes.Scene(f"assets\{b}ackgrounds\default_battlefield.png")
default.spawnX1 = 280; default.spawnY1 = 294; default.spawnX2 = 970; default.spawnY2 = 294
barrierT_1 = default.Barrier(550,102,733,124)
barrierL_1 = default.Barrier(340,218,528,238)
barrierR_1 = default.Barrier(756,218,944,237)
barrierM1_1 = default.Barrier(252,355,1016,412)
#barrierM2_1 = default.Barrier(311,317,913,458)
barrierM3_1 = default.Barrier(375,461,890,484)
barrierM4_1 = default.Barrier(435,494,772,546)
barrierM5_1 = default.Barrier(587,555,711,657)
default.barriers = [barrierT_1,barrierL_1,barrierR_1,barrierM1_1,barrierM3_1,barrierM4_1,barrierM5_1]

b='b';f='f';finalDest = classes.Scene(f"assets\{b}ackgrounds\{f}inal_destination.jpg")
finalDest.spawnX1 = 405; finalDest.spawnY1 = 443; finalDest.spawnX2 = 835; finalDest.spawnY2 = 443
barrierM1_2 = finalDest.Barrier(354,484,929,535)
barrierM2_2 = finalDest.Barrier(401,543,880,612)
barrierM3_2 = finalDest.Barrier(532,621,727,685)
finalDest.barriers = [barrierM1_2,barrierM2_2,barrierM3_2]

b='b';f='f';fountain = classes.Scene(f"assets\{b}ackgrounds\{f}ountain_of_dreams.jpg")
fountain.spawnX1 = 400; fountain.spawnY1 = 448; fountain.spawnX2 = 860; fountain.spawnY2 = 448
barrierT_3 = fountain.Barrier(573,298,706,308)
barrierR_3 = fountain.Barrier(759,402,893,411)
barrierL_3 = fountain.Barrier(387,402,521,411)
barrierC1_3 = fountain.Barrier(574,394,707,437)
barrierM1_3 = fountain.Barrier(350,489,923,716)
fountain.barriers = [barrierT_3,barrierR_3,barrierL_3,barrierC1_3,barrierM1_3]

b='b';f='f';luigi = classes.Scene(f"assets\{b}ackgrounds\luigi_mansion.jpg")
luigi.spawnX1 = 300; luigi.spawnY1 = 459; luigi.spawnX2 = 950; luigi.spawnY2 = 459
barrierT_4 = fountain.Barrier(345,370,938,387)
barrierL_4 = fountain.Barrier(537,445,599,458)
barrierR_4 = fountain.Barrier(684,447,741,457)
barrierM1_4 = fountain.Barrier(246,500,1039,533)
barrierM2_4 = fountain.Barrier(229,540,1037,713)
luigi.barriers = [barrierT_4,barrierL_4,barrierR_4,barrierM1_4,barrierM2_4]

scenes = [default,finalDest,fountain,luigi]

if 脑子 == "smart":
    脑子 = "Found"

home = True # Home screen
running = False # Main game
choose_map = False # Map selection
selection = False # Character selection
end = False # End screen


P1 = characters[0]
P2 = characters[1]

#changing map size for preview
b = 'b'; f = 'f'
original_map0 = pygame.image.load(f"assets\{b}ackgrounds\default_battlefield.png")
original_map1 = pygame.image.load(f"assets\{b}ackgrounds\{f}inal_destination.jpg")
original_map2 = pygame.image.load(f"assets\{b}ackgrounds\{f}ountain_of_dreams.jpg")
original_map3 = pygame.image.load(f"assets\{b}ackgrounds\luigi_mansion.jpg")
original_map4 = pygame.image.load(f"assets\{b}ackgrounds\chinese_mountains.jpeg")
map0 = pygame.transform.scale(original_map0,(256,144))
map1 = pygame.transform.scale(original_map1,(256,144))
map2 = pygame.transform.scale(original_map2,(256,144))
map3 = pygame.transform.scale(original_map3,(256,144))
map4 = pygame.transform.scale(original_map4,(256,144))

while home:
    # Load Homepage
    screen.blit(homepage,(0,0))
    
    # Watch for events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            choose_map = True
            home = False
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("assets\music\Poems_of_a_Machine.mp3")
            pygame.mixer.music.play()

        # Exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

while True:
    #resets the music
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load("assets\music\Poems_of_a_Machine.mp3")
    pygame.mixer.music.play()
    
    
    while choose_map: # Choose the map
        screen.fill("gray")

        # Loads maps
        screen.blit(map0,(150,100))
        screen.blit(map1,(500,100))
        screen.blit(map2,(850,100))
        screen.blit(map3,(325,450))
        screen.blit(map4, (675,450))

        for event in pygame.event.get(): # Respond to events
            mouse_x, mouse_y = pygame.mouse.get_pos() # Sets mouse coords

            # If you click on a map, that map will be the map and the screen will switch to character selection
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x in range(150,400) and mouse_y in range(100,350):
                    selectedScene = scenes[0]
                    selection = True
                    choose_map = False
                if mouse_x in range(500,750) and mouse_y in range(100,350):
                    selectedScene = scenes[1]
                    selection = True
                    choose_map = False
                if mouse_x in range(850,1100) and mouse_y in range(100,350):
                    selectedScene = scenes[2]
                    selection = True
                    choose_map = False
                if mouse_x in range(325,575) and mouse_y in range(450,700):
                    selectedScene = scenes[3]
                    selection = True
                    choose_map = False
                '''
                if mouse_x in range(675,575) and mouse_y in range(925,700):
                    selectedScene = scenes[4]
                    selection = True
                    choose_map = False
                '''

            # Exit game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    times_clicked = 0 # counts times the mouse was clicked for character selection

    while selection:
        # Character Select screen
        screen.fill("red")

        #text("CHOOSE YOUR CHARACTER",640,100)
        ID1 = pygame.image.load("assets\holder.jpeg")
        ID2 = pygame.image.load("assets\characters\AmongUs\Amogus_ID.png")
        ID3 = pygame.image.load("assets\holder.jpeg")
        screen.blit(ID1,(150,100))
        screen.blit(ID2,(500,100))
        screen.blit(ID3,(850,100))

        # Tells the players (you) which player is picking the character
        if times_clicked == 0:
            screen.blit(nametag_P1, (mouse_x+10,mouse_y+10))
        else:
            screen.blit(nametag_P2, (mouse_x+10,mouse_y+10))

        # Choose the character here
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            #If you click a character, that will set it as P1 or P2 based on times_clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x in range(150,300) and mouse_y in range(100,350):
                    if times_clicked == 0:
                        P1 = characters[0]
                    else:
                        P2 = characters[0]
                    times_clicked+=1
                if mouse_x in range(500,750) and mouse_y in range(100,350):
                    if times_clicked == 0:
                        P1 = characters[1]
                    else:
                        P2 = characters[1]
                    times_clicked+=1
                if mouse_x in range(850,1100) and mouse_y in range(100,350):
                    times_clicked+=1
                
                # Sets P1 and P2 images for later
                P1_image_og = pygame.image.load(P1.imagePaths[0])
                P1_image = pygame.transform.scale(P1_image_og, (50,60))

                P2_image_og = pygame.image.load(P2.imagePaths[0])
                P2_image = pygame.transform.scale(P2_image_og, (50,60))

                # Goes to game after selecting characters
                if times_clicked == 2:
                    running = True
                    selection = False

                    # Music based on which background was chosen earlier
                    if selectedScene == scenes[0]:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load("assets\music\Pokemon.mp3")
                        pygame.mixer.music.play()
                    if selectedScene == scenes[1]:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load("assets\music\Sky_Fortress.mp3")
                        pygame.mixer.music.play()
                    if selectedScene == scenes[2]:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load("assets\music\Diamond_Eyes.mp3")
                        pygame.mixer.music.play()
                    if selectedScene == scenes[3]:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load("assets\music\Super_Mario_Bros.mp3")
                        pygame.mixer.music.play()
                    '''
                    if selectedScene == scenes[4]:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        pygame.mixer.music.load("assets\music\Pokemon.mp3")
                        pygame.mixer.music.play()
                    '''
        # Exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        
        ## Players
        spawnX1 = selectedScene.spawnX1; spawnY1 = selectedScene.spawnY1; spawnX2 = selectedScene.spawnX2; spawnY2 = selectedScene.spawnY2
        player = classes.Player(spawnX1,spawnY1,P1)
        player2 = classes.Player(spawnX2,spawnY2,P2)
        players = [player,player2]

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    #resets player scores
    player.score = 0
    player2.score = 0

    while running:
        # SETUP
        screen.fill(background)
        selectedScene.update(screen)

        # Player statistics
        # P1
        P1_stats = big_font.render(str(int(player2.hp)), False, "red")
        P1_lives = big_font.render("Lives = " + str(3 - player2.score), False, "red")
        pygame.draw.circle(screen, (50,50,50), (100,660), 70, 0)
        pygame.draw.circle(screen, "white", (100,660), 70, 5)
        screen.blit(P1_image,(75,630))
        screen.blit(P1_stats,(125,660))
        # P2
        P2_stats = big_font.render(str(int(player.hp)), False, "red")
        P1_lives = big_font.render("Lives = " + str(3 - player2.score), False, "red")
        pygame.draw.circle(screen, (50,50,50), (1205,660), 70, 0)
        pygame.draw.circle(screen, "white", (1205,660), 70, 5)
        screen.blit(P2_image,(1180,630))
        screen.blit(P2_stats,(1230,660))

        # Nametag
        screen.blit(nametag_P1, (player.x + 7, player.y - 22))
        screen.blit(nametag_P2, (player2.x + 7, player2.y - 22))

        # WATCH FOR EVENTS HERE (CONDITIONALS SECTION)
        for event in pygame.event.get(): # BUG: this loop only runs when there are events, not always.
            running = functions.quitCheck(event,running)
            functions.moveCheck(event,players[0],players[1])
            functions.attackCheck(event,players[0],players[1])
        
        for character in players:
            for barrier in selectedScene.barriers:
                barrier.solidify(screen,character,players)


        # RENDER GAME OBJECTS HERE
            character.update(screen,character,players)

        # If someone dies goes to end screen
        if player.score == 1 or player2.score == 3:
            screen.blit(pygame.image.load("assets\holder.jpeg"), (640,360))
            end = True
            running = False
            pygame.time.wait(3000)
        

        # UPDATE SCREEN
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    #pygame.quit()

    while end:
        screen.fill("white")
        screen.blit(pygame.image.load("assets\holder.jpeg"), (360,360))
        winner = big_font.render("WINNER", True, "black", "yellow")
        boo = big_font.render("BOO", True, "black", "red")
        '''
        # shows the winner
        if P1_lives == 0 and P2_lives > 0:
            screen.blit(P1_image,(640,360))
            screen.blit(winner,(640,360))
        if P2_lives == 0 and P1_lives > 0:
            screen.blit(P2_image,(640,360))
            screen.blit(winner,(640,360))
        if P1_lives and P2_lives == 0:
            screen.blit(P1_image,(600,360))
            screen.blit(P2_image,(680,360))
            screen.blit(boo,(640,360))
        '''
        # Quit game or Play again
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_x in range(600):# and mouse_y in range(100,200): #coord tbd
                    end = False
                    pygame.quit()
                if mouse_x in range(600,1280):# and mouse_y in range(360):
                    choose_map = True
                    end = False

        # UPDATE SCREEN
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
