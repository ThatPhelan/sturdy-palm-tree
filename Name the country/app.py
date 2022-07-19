import pygame, sys
from pygame.locals import*
pygame.init()
FPS = 101
clock = pygame.time.Clock()

start = 6000

#15 minute timer
number15 = 15


#Display
bg = (255, 255, 255)
win = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("app")
win.fill(bg)
worldmap = pygame.image.load("map.jpg")
worldmap = pygame. transform. scale(worldmap, (1500, 600))

#List of countries
countries = ['afghanistan','albania','algeria','andorra','angola','antigua and barbuda','argentina','armenia','australia','austria','azerbaijan','bahamas','bahrain','bangladesh',
'barbados','belarus','belgium','belize','benin','bhutan','bolivia','bosnia and herzegovina','botswana','brazil','brunei','bulgaria','burkina faso','burundi','cambodia',
'cameroon','canada','cape verde','central african republic','chad','chile','china','colombia','comoros','republic of congo','democratic republic of the congo','costa rica',
'croatia','cuba','cyprus','czech republic','denmark','djibouti','domninica', 'dominican republic','east timor', 'ecuador','egypt','el salvador','equatorial guinea',
'eritrea','estonia','ethiopia','fiji','finland','france','gabon','gambia','georgia','germany','ghana','greece','grenada','guatemala','guinea','guinea bissau','guyana',
'haiti','honduras','hungary','iceland','india','indonesia','iran','iraq','ireland','israel','italy','ivory coast','jamaica','japan','jordan','kazakhstan','kenya','kiribati',
'north korea', 'south korea','kosovo','kuwait','kyrgyzstan','laos','latvia','lebanon','lesotho','liberia','libya','liechtenstein','lithuania','luxembourg','macedonia',
'madagascar','malawi','malaysia','maldives','mali','malta','marshall islands','mauritania','mauritius','mexico','micronesia','moldova','monaco','mongolia','montenegro',
'morocco','mozambique','myanmar','namibia','nauru','nepal','netherlands','new zealand','nicaragua','niger','nigeria','norway','oman','pakistan','palau','panama','palestine','papua new guinea',
'paraguay','peru','philippines','poland','portugal','qatar','romania','russia','rwanda','st kitts and nevis','st lucia','st vincent','samoa','san marino','sao tome',
'saudi arabia','senegal','serbia','seychelles','sierra leone','singapore','slovakia','slovenia','solomon islands','somalia','south africa','south sudan','spain','sri lanka',
'sudan','suriname','swaziland','sweden','switzerland','syria','taiwan','tajikistan','tanzania','thailand','togo','tonga','trinidad and tobago','tunisia','turkey','turkmenistan',
'tuvalu','uganda','ukraine','uae','uk','usa','uruguay','uzbekistan','vanuatu','vatican','venezuela','vietnam','yemen','zambia','zimbabwe']

#Scoreboard
font = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 20)
winlose_font = pygame.font.Font(None, 200)
live_score = 0
def scoreboard(msg, color_active):
    pygame.draw.rect(win,(255, 255, 255),[1080,10,450,50])
    score = font.render(str(live_score), True, color_active)
    score_pos = (1120, 25)
    score2 = font.render(("/197"), True, color_active)
    score2_pos = (1140, 25)
    
    scoretext = font2.render(("score"), True, (155,155,155))
    scoretext_pos = (1142, 11)
     
    
    if live_score in range(10, 100):
        score_pos = (1100, 25)
    if live_score >= 100:
        score_pos = (1080, 25)   
    
    win.blit(score2,score2_pos)
    win.blit(score, score_pos)
    win.blit(scoretext, scoretext_pos)
    

def timer():
    #Text that says "Timer"
    timertext = font2.render("Timer", True, (155,155,155))
    timertext_pos = (1377, 11)
    #Minute timer
    cover = (1442, 10, 50, 50)
    countdown = font.render(str(start), True, color_active)
    countdown_pos = (1404, 25)
    

    leftzero = font.render("0", True, color_active)
    if start < 1000:
        countdown_pos = (1421, 25)
        win.blit(leftzero, (1402, 25))
    else:
        countdown_pos = (1404, 25)
    if start > 2000:
        cover = (1443, 10, 50, 50)

    #Colon
    colon = font.render(":", True, color_active)
    colon_pos = (1390, 25)
    win.blit(colon, colon_pos)
    
    #15 minute timer
    fifteen = font.render(str(number15), True, color_active)
    fifteen_pos = (1350, 25)
    
    if number15 < 10:
        fifteen_pos = (1371, 25)
    elif number15 > 10:
        fifteen_pos = (1350,25)
    if number15 == 0:
        print("you lost")

    win.blit(fifteen, fifteen_pos)

    win.blit(countdown,countdown_pos)

    win.blit(timertext, timertext_pos)

    #Covers the number 6 with a 0 when at 60 seconds
    if start == 6000:
        pygame.draw.rect(win,(255, 255, 255),(1404, 25, 20,50))
        win.blit(leftzero,(1404, 25))
    
    if start <= 100:
        pygame.draw.rect(win,(255, 255, 255),[1421,25, 28, 30])
        rightzero = font.render(("0"), True, color_active)
        win.blit(rightzero, (1420, 25))
    #milisecond cover
    pygame.draw.rect(win,(255, 255, 255),cover)
    

font3 = pygame.font.Font(None, 300)
starttext = font.render(("Press Space to begin"), True, (0,0,0))
starttext_pos = (580, 650)
starting = False


       

    
#Entry box
input_rect = pygame.Rect(0,25,140,32)
color_active = (0,0,0)
color_passive = (155,155,155)
color = color_passive
active = False
inputfont = pygame.font.Font(None, 32)
user_text = ''



#print(pygame.font.get_fonts())


#Gameloop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #checks if your clicking on the entry box
        if event.type == pygame.MOUSEBUTTONDOWN and number15 < 15   :
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        #key input for entry box
        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                else:
                    user_text += event.unicode    
   
    #   #press space to begin
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and number15 == 15:
                
                number15 -= 1
                starting = True
                
                print(10)
    
    #Once space is pressed the timer starts and stops the timer once you've guessed all countries
    if number15 < 15 and number15 >= 0 and len(countries) > 0:
        start -= 1
    
    #
    

    if active:
        color = color_active
    else:
        color = color_passive
    #entrybox eraser
    pygame.draw.rect(win,(255, 255, 255),[0,25,500,50])
    
    win.blit(worldmap, (50, 150))
    #Starts the timer and erases the "Press space to start" text.
    if starting == False:
        
        win.blit(starttext,starttext_pos)
   

    scoreboard(None, (0,0,0))
    timer()
    if start <= 0 and number15 >= 0:
        number15 -= 1
    pygame.draw.rect(win,color,input_rect,2)

    text_surface =  inputfont.render(user_text,True,(0,0,0))
    win.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    
    input_rect.w = max(100,text_surface.get_width() + 10)
    


    
    
    if start <= 0 and number15 >= 0:
        start = 6000
    
    if number15 == 0 and start == 0:
        running = False
        print("You lost stinky los")
        losingtext = winlose_font.render('Game over', True, color_active)
        win.blit(losingtext,(385, 350))
    #
    
    if user_text in countries and number15 < 15:
        countries.remove(user_text)
        live_score +=1
        user_text = ''
    if len(countries) == 0:
        wintext = winlose_font.render('You Won!', True, color_active)

        win.blit(wintext,(385, 350))
        
        print("You won!")
        #running = False
    pygame.display.update()
    clock.tick(FPS)
print(len(countries))