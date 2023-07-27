#imports that are used for games
import pygame
from pygame import *
from math import *
import random

#defining colors
WHITE= (255, 255, 255)
BLACK=(0, 0, 0)
GREY=(128,128,128)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
YELLOW=(239,225,28)
PURPLE=(102,0,204)
ORANGE=(255,128,0)

#defining things that are needed for the game to be visable( ex. makes the screen dimensions)
init()
size = (900, 700)
screen = display.set_mode(size, RESIZABLE)
clock =time.Clock()

#creates a button that when clicked performs an action
def button(msg,x,y,w,h,col,font_col,action=None,*argv): 
    args=()
    pos_mouse = mouse.get_pos()
    click = mouse.get_pressed()
    text=draw_text(msg, 'Calibri', 25,font_col)
    txt_w=text[1]
    txt_h=text[2]
    draw.rect(screen, col,(x,y,w,h))
    if  x+w > pos_mouse[0] > x and y+h > pos_mouse[1] > y:
        if click[0]==1 and action!=None:
            ret=action(*argv)
            if ret!=None:
                return ret
    screen.blit(text[0], [int((w-txt_w)/2+x),int((h-txt_h)/2+y)])

#writes anything somewhere, simplyfies the process to only a few lines instead of like 10. Set a variable equal to draw_text, then scren.blit using the the first object in the variable    
def draw_text(msg, font, size,color):
    text_font= pygame.font.SysFont(font, size, True, False)
    text = text_font.render(msg,True,color)
    text_dim=[]
    text_dim.append(text)
    text_dim.append(text.get_rect().width)
    text_dim.append(text.get_rect().height)
    return text_dim


#quites the game, makes it one line instead of two and makes it easier to remember and able to be on a button
def quitgame():
    pygame.quit()
    quit()

#writes a number to the screen to give hints about locations of bombs
def write_num(num,x,y):
    if num==1:
        text=draw_text(str(num),'calibri',50,BLUE)
        screen.blit(text[0],[int(x+(50-text[1])/2),int(y+(50-43)/2)])
    elif num==2:
        text=draw_text(str(num),'calibri',50,GREEN)
        screen.blit(text[0],[int(x+(50-text[1])/2),int(y+(50-43)/2)])
    elif num==3:
        text=draw_text(str(num),'calibri',50,ORANGE)
        screen.blit(text[0],[int(x+(50-text[1])/2),int(y+(50-43)/2)])
    elif num==4:
        text=draw_text(str(num),'calibri',50,RED)
        screen.blit(text[0],[int(x+(50-text[1])/2),int(y+(50-43)/2)])
    elif num==5:
        text=draw_text(str(num),'calibri',50,PURPLE)
        screen.blit(text[0],[int(x+(50-text[1])/2),int(y+(50-43)/2)])
    elif num==6:
        text=draw_text(str(num),'calibri',50,YELLOW)
        screen.blit(text[0],[int(x+(50-text[1])/2),int(y+(50-43)/2)])
    elif num==7:
        text=draw_text(str(num),'calibri',50,BLACK)
        screen.blit(text[0],[int(x+(50-text[1])/2),int(y+(50-43)/2)])
    elif num==8:
        text=draw_text(str(num),'calibri',50,GREY)
        screen.blit(text[0],[int(x+(50-text[1])/2),int(y+(50-43)/2)])


#checks how many bombs are nearby or just returns the cells touching a certain cell
def check_nearby(cells,cell,check):
    score=0
    nearby=[]
    if cell["index"]%18==0:
        nearby.append(cell["index"]+1)
        nearby.append(cell["index"]-17)
        nearby.append(cell["index"]-18)
        nearby.append(cell["index"]+18)
        nearby.append(cell["index"]+19)
    elif cell["index"]%18==17:
        nearby.append(cell["index"]-1)
        nearby.append(cell["index"]-18)
        nearby.append(cell["index"]-19)
        nearby.append(cell["index"]+17)
        nearby.append(cell["index"]+18)
    else:        
        nearby.append(cell["index"]-1)
        nearby.append(cell["index"]+1)
        nearby.append(cell["index"]-17)
        nearby.append(cell["index"]-18)
        nearby.append(cell["index"]-19)
        nearby.append(cell["index"]+17)
        nearby.append(cell["index"]+18)
        nearby.append(cell["index"]+19)
    if check=="bomb":
        for i in nearby:
            #print(i)
            try:
                if i>=0:
                    if cells[i]["bomb"]==True:
                        score+=1
            except IndexError:
                pass
        return score
    elif check=="open":
        return nearby

#Checks if the player has one
def win_check(cells):
     for i in range(252):
            if cells[i]["bomb"]==False and cells[i]["covered"]==True:
                return False
            else:
                pass
    

#draws the bombs
def draw_bomb(x,y):
    #draw.ellipse(screen, BLACK, [x,y,30,30], 0)
    draw.circle(screen, BLACK, [x+25,y+33],15, 0)
    draw.rect(screen, GREY,[x+22,y+3,6,15],0)
    draw.line(screen,BLACK,[x+22,y+8],[x+27,y+8],1)
    draw.line(screen,BLACK,[x+22,y+13],[x+27,y+13],1)
    draw.line(screen,BLACK,[x+22,y+18],[x+27,y+18],1)
    
#draws flag
def draw_flag(x,y):
    draw.polygon(screen,RED,[[x+20,y+5], [x+20,y+25], [x+40,y+15]])
    draw.line(screen,BLACK,[x+20,y+5],[x+20,y+45],1)
    draw.line(screen,BLACK,[x+10,y+45],[x+30,y+45],3)
    
#used to unpause game, need function to use in button
def unpause(paused):
    paused=False
    
    return paused

#pause screen
def pause(): 
    paused=None
    x=1
    y=1
    while paused==None:    
        pos_mouse= mouse.get_pos()
        x_mouse=pos_mouse[0]
        y_mouse=pos_mouse[1]
        screen = display.set_mode(size)
        for event in pygame.event.get():

            if event.type == QUIT: # If user clicked close
                quitgame()
                # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                paused=False
            

        draw.rect(screen, GREY, [300,100,300,400]) #size
        pause_txt=draw_text("Paused", 'calibri', 35, RED) #size maybe
        pause_txt_w=pause_txt[1]
        screen.blit(pause_txt[0], [(size[0]-pause_txt_w)/2, size[1]*5/28])
        paused=button("continue",size[0]*4/9,size[1]*2/7,size[0]/9,size[1]/36,GREEN,BLACK,unpause,paused)#size  
        button("quit",size[0]*4/9,size[1]*4/7,size[0]/9,size[1]/36,RED,BLACK,quitgame) #size
        button("Restart", size[0]*4/9, size[1]*3/7, size[0]/9,size[1]/36, YELLOW, BLACK, main) #size
        
        display.flip()
     
        
        clock.tick(60)
        
#intro screen
def intro():
    done = False
    while not done:    
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                done= True
        title = draw_text("Mine Sweeper", 'Calibri', 50, BLACK) 
        screen.blit(title[0], [300, 100])
        button("Start",300,300,100,50,GREEN,BLACK,main)
        button("Quit",500,300,100,50,RED,BLACK,quitgame)
        draw_flag(430,200)
        display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)

#main game screen
def main():
    main_done = False
    screen = display.set_mode(size)
    cells=[]
    cell={}
    x=0
    y=0
    num=0
    numbers=[]
    bomb_count=0
    
    #makes list of each cell in game, tells where each cell is, if it has been uncovered, if it has a bomb and if it has a flag and if it has a number.
    for i in range(252):
        numbers.append(i)
        cell={"index":i,"l":x,"r":x+50,"t":y,"b":y+50,"covered":True,"bomb":False,"flag":False,"num":""}
        cells.append(cell)
        x+=50
        if x==900:
            y+=50
            x=0
  #picks where bombs will go randomly
    num=random.sample(numbers,k=40)
    for i in num:
        cells[i]["bomb"]=True
        
##    #checks number of bombs
##    for i in range(252):
##        if cells[i]["bomb"]==True:
##            bomb_count+=1
    #print(bomb_count)

    while not main_done:    
        x=0
        y=0    
        screen.fill(WHITE)
        pos= mouse.get_pos()
        x_mouse=pos[0]
        y_mouse=pos[1]
        click = mouse.get_pressed()
        
        for event in pygame.event.get():

            if event.type == QUIT: # If user clicked close
                quitgame()
                # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                quitgame()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused=True
                    pause()

            for i in range(len(cells)):
                if event.type==MOUSEBUTTONDOWN and event.button == 1 and x_mouse>cells[i]["l"] and x_mouse<cells[i]["r"] and y_mouse>cells[i]["t"] and y_mouse<cells[i]["b"]:
                           cells[i]["covered"]=False
                elif event.type==MOUSEBUTTONDOWN and event.button == 3 and x_mouse>cells[i]["l"] and x_mouse<cells[i]["r"] and y_mouse>cells[i]["t"] and y_mouse<cells[i]["b"] and cells[i]["flag"]==False:
                           cells[i]["flag"]=True
                elif event.type==MOUSEBUTTONDOWN and event.button == 3 and x_mouse>cells[i]["l"] and x_mouse<cells[i]["r"] and y_mouse>cells[i]["t"] and y_mouse<cells[i]["b"] and cells[i]["flag"]==True:
                    cells[i]["flag"]=False

##        cells[6]["covered"]=False
##        cells[5]["flag"]=True
                           
##        cells[0]["bomb"]=True
##        cells[2]["bomb"]=True
##        cells[19]["bomb"]=True
##        cells[18]["bomb"]=True
##        cells[20]["bomb"]=True
##        cells[36]["bomb"]=True
##        cells[37]["bomb"]=True
##        cells[38]["bomb"]=True
##        num=bomb_check(cells,cells[37])
##        print(num)

#draws bombs, flags, numbers and squares where they need to go
        for i in range(252):
            
            if cells[i]["bomb"]==True:
                draw_bomb(cells[i]["l"],cells[i]["t"])
            if cells[i]["bomb"]==False:
                number=check_nearby(cells,cells[i],"bomb")
                if number==0:
                    if cells[i]["covered"]==False:
                        nearby=check_nearby(cells,cells[i],"open")
                        try:
                            for j in nearby:
                                if j>=0:
                                    cells[j]["covered"]=False
                                
                        except IndexError:
                            pass
                else:
                    write_num(number,cells[i]["l"],cells[i]["t"])
            
            if cells[i]["covered"]==True:
                draw.rect(screen,GREY,[cells[i]["l"],cells[i]["t"],50,50],0)
            if cells[i]["flag"]==True:
                draw_flag(cells[i]["l"],cells[i]["t"])

        #draws grid lines
        for i in range(0,900,50):
            draw.line(screen,BLACK,[i,0],[i,700],1)
        for i in range(0,700,50):
            draw.line(screen,BLACK,[0,i],[900,i],1)

#checks for a won game
        win=win_check(cells)
        #print(win)
        if win==None:
            finish("win")
            
        
        #check if lost game 
        for i in range(252):
            if cells[i]["bomb"]==True and cells[i]["covered"]==False:
                finish("lose")
        # --- Go ahead and update the screen with what we've drawn.
        display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)

#end of game screen
def finish(result):
    finish_done=False
    size=pygame.display.get_surface().get_size()
    screen = display.set_mode(size,RESIZABLE)
    while not finish_done:
        
        for event in pygame.event.get():
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                size=pygame.display.get_surface().get_size()
                pygame.display.flip()
            if event.type== KEYDOWN and event.key==K_RETURN:
                main()
            if event.type == QUIT: # If user clicked close
                quitgame()
                # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                quitgame()
        
        if result=="win":
            screen.fill(GREEN)
            draw.rect(screen, BLACK, [300, 250, 300, 200], 0)
            win=draw_text("You Won!!", 'calibri', 35,GREEN) #size maybe
            win_w=win[1]
            screen.blit(win[0], [(size[0]-win_w)/2, size[1]*5/14])
        elif result=="lose":
            screen.fill(RED)
            draw.rect(screen, BLACK, [300, 250, 300, 200], 0)
            lose=draw_text("You Lose", 'calibri', 35, RED) #size maybe
            lose_w=lose[1]
            screen.blit(lose[0], [(size[0]-lose_w)/2, size[1]*5/14])
        button("quit",size[0]*4/9,size[1]*4/7,size[0]/9,size[1]/28,RED,BLACK,quitgame) #size
        button("Restart", size[0]*4/9, size[1]*3/7, size[0]/9,size[1]/28,YELLOW, BLACK, main) #size
        display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
  
intro()
quit()
