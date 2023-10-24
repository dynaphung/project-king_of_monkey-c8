#============================ IMPORTS ============================
import tkinter as tk
from tkinter import * 
from tkinter import Scrollbar
from PIL import ImageTk, Image

#============================ CONSTANTS ============================

WINDOW_WIDTH=1420
WINDOW_HEIGHT=800

GRAVITY_FORCE = 9
JUMP_FORCE = 35
SPEED = 5
TIMED_LOOP = 6


keyPressed = []
#============================ GLOBAL ============================
score=0

#============================ MAIN WINDOW ============================
window = tk.Tk()
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
window.title("ADVANTURE GAME")
frame = tk.Frame()
canvas = tk.Canvas(frame)


#============================ IMAGES ============================
                #=======BACK GROUND=============
home_bg = PhotoImage(file='Images/bg_home.png')
bg=PhotoImage(file="Images/bg_choose-hero.png")
bg_level=PhotoImage(file="Images/bg_level.png")
bg_level1=PhotoImage(file="Images/level1.png")
bg_level2=PhotoImage(file="Images/level2.png")
bg_level3=PhotoImage(file="Images/level3.png")
winter_bg=PhotoImage(file="Images/winter_bg.png")

                #=======PLAYER IMAGES===========
player1_img=PhotoImage(file="Images/player1.png")
player2_img=PhotoImage(file="Images/player2.png")
player3_img=PhotoImage(file="Images/player3.png")

                #=======SIGN IMAGES=============
check=PhotoImage(file="Images/accept.png")
next_img=PhotoImage(file="Images/next.png")
bord_name=PhotoImage(file="Images/bord_name.png")
start_img = PhotoImage(file="Images/start-button.png")
help_btn = PhotoImage(file="Images/help-button.png")
exit_img = PhotoImage(file="Images/exit-button.png")
back_img = PhotoImage(file="Images/back.png")
help_board = PhotoImage(file="Images/help.png")

                #IMAGES IN GAMES
ground_wall=PhotoImage(file="Images/grass.png")
land_image=PhotoImage(file="Images/land.png")
stone_img=PhotoImage(file="Images/stone.png")
wall_img=PhotoImage(file="Images/big_stone.png")
fire_img=PhotoImage(file="Images/fire.png")
key_img = PhotoImage(file="Images/key.png")
# snow_bg = PhotoImage(file="Images/snow_bg.png")
ice_stone = PhotoImage(file="Images/ice_stone.png")
ice_thorn = PhotoImage(file="Images/ice_thorn.png")

banana_img=PhotoImage(file="Images/banana.png")

#============================= BACKGROUND =====================
canvas_bg_level2 = canvas.create_image(0,0,image=bg_level1,anchor=NW)
canvas_bg1_level2 = canvas.create_image(1340,0,image=bg_level1,anchor=NW)
canvas_bg1_level2 = canvas.create_image(2400,0,image=bg_level1,anchor=NW)
canvas_bg_level2 = canvas.create_image(3540,0,image=bg_level1,anchor=NW)

# Auto-scrolling--------------------
scrollbar_bottom = Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

#=========================== ALL LEVELS =======================

def level1(event):
    global background1, background2, player, score_id
    
    #====================score================
    score_id = canvas.create_text(170, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_level1, anchor="nw")
    # canvas.create_image(50,360,image=player1_img, anchor="nw",tags="players1")
    #============= LAND IMAGES =============
    # canvas.create_image(300,100,image=land_image, anchor="nw",tags="platform")
    canvas.create_image(850,400, image = stone_img, anchor="nw", tags = "plateform")
    
    #============ ANERMY IMAGES ==============
    canvas.create_image(400,490,image=fire_img, anchor="nw", tags="anermy")
    
    #============ FRUIT IMAGES ===============
    canvas.create_image(680,550,image=banana_img,tags="score")
    canvas.create_image(950,400,image=banana_img,tags="score")
    #============= UNDER GROUND ============
    canvas.create_image(-50,600,image=ground_wall, anchor="nw", tags="plateform")
    canvas.create_image(350,600,image=ground_wall, anchor="nw", tags="plateform")
    
    #============= BACK SIGN ===============
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")
    
    player = canvas.create_image(10,150, image =player1_img, anchor="nw")
    window.after(TIMED_LOOP, gravity)  

def level2(event):
    canvas.create_image(1, 0, image=bg_level2, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")

def level3(event):
    canvas.delete("all")
    canvas.create_image(1, 0, image=bg_level3, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")

#============================ SELECT PLAYER ============================
def selectPlayer():
    canvas.delete("all")
    # canvas.create_image(0, 1, image=bg, anchor="nw")
    canvas.create_image(0,0, image=bg, anchor="nw")
    canvas.create_text(720, 100, text="CHOOSE AVATAR", font=("airal", 70, "bold"),fill="yellow")
                            #==== BACK HOME =====
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
                            #==== PLAYER 1 =====
    canvas.create_image(320, 220, image=player1_img, anchor="nw", tags="player1")
    canvas.create_image(350, 450, image=bord_name, anchor="nw", tags="player1")
    canvas.create_text(440, 485, text="NAVY", font=("airal", 25, "bold"), fill="#8D4004",tags="player1")
                            #==== PLAYER 2 =====
    canvas.create_image(620, 220, image=player2_img, anchor="nw", tags="player2")
    canvas.create_image(650, 450, image=bord_name, anchor="nw", tags="player2")
    canvas.create_text(740, 485, text="NARTIH", font=("airal", 25, "bold"), fill="#8D4004",tags="player2")
                            # ==== PLAYER 3 =====
    canvas.create_image(920, 220, image=player3_img, anchor="nw", tags="player3")
    canvas.create_image(950, 450, image=bord_name, anchor="nw", tags="player3")
    canvas.create_text(1040, 485, text="BOYLOY", font=("airal", 25, "bold"), fill="#8D4004",tags="player3")
    
                            #==== NEXT =====
    canvas.create_image(1260, 610, image=next_img, anchor="nw", tags="next")

#PLAYER 1  
def player1(event):
    global player
    canvas.delete("all")
    # player=PLAYER1_CELL
    selectPlayer()
    canvas.create_image(390, 500, image=check, anchor="nw")
 
#PLAYER 2  
def player2(event):
    global player
    canvas.delete("all")
    selectPlayer()
    canvas.create_image(690, 500, image=check, anchor="nw")

#PLAYER 3
def player3(event):
    global player
    canvas.delete("all")
    selectPlayer()
    canvas.create_image(990, 500, image=check, anchor="nw")


# ======================= HOME_PAGE =============================
def home():
    canvas.create_image(0,0, image=home_bg, anchor="nw")
    canvas.create_image(610, 350, image=start_img, anchor="nw", tags="start")
    canvas.create_image(600, 450, image=help_btn, anchor="nw", tags="help")
    canvas.create_image(615, 550, image=exit_img, anchor="nw", tags="exit")

# ======================= BACK TO LEVELS PAGE =============================
def backTolevel(event):
    allLevels()

def help(event):
    canvas.create_image(1, 0, image=winter_bg, anchor="nw")
    canvas.create_image(380,100, image = help_board, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
def start(event):
    selectPlayer()
    
def backHome(event):
    home()


#============================ EXIT ============================
def exit(event):
    window.destroy()


#============================ ALL LEVELS BUTTON ============================
def allLevels():
    
    canvas.create_image(1, 0, image=bg_level, anchor="nw")
                            #==== LEVEL 1 =====
    canvas.create_image(620, 150, image=bord_name, anchor="nw", tags="level1")
    canvas.create_text(700, 185, text="Level 1", font=("arsenal", 20, "bold"), fill="white",tags="level1")
                            #==== LEVEL 2 =====
    canvas.create_image(620, 300, image=bord_name, anchor="nw", tags="level2")
    canvas.create_text(700, 335, text="Level 2", font=("arsenal", 23, "bold"), fill="white",tags="level2")
                            #==== LEVEL 3 =====
    canvas.create_image(620, 450, image=bord_name, anchor="nw", tags="level3")
    canvas.create_text(700, 485, text="Level 3", font=("arsenal", 23, "bold"), fill="white",tags="level3")
                            #==== BACK BUTTON=====
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_player")
    
# =============================NEXT============================
def next(event):
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    allLevels()

#BACK PLAYER
def backPlayer(event):
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    selectPlayer()
#=========================== FUNCTIONS MOVE PLAYER =======================
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("plateform")
    if coord[0] + dx < 0 or coord[1] + dx > WINDOW_WIDTH:
        return False
    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player1_img.width(), (coord[1] - 50) + player1_img.height() + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]+ player1_img.width() + dx, (coord[1] - 50) + player1_img.height())
    for platform in platforms:
        if platform in overlap:
            return False
    return True

def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)
# ----------------start_move------------------------
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()
#---------------Move_object----------------------------------
def move():
    
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            # canvas.itemconfig(player, image = player_left)
            x -= SPEED
        if "Right" in keyPressed:
            # canvas.itemconfig(player, image = player_img)
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player, x, 0)
            window.after(TIMED_LOOP, move)
            
#--------check_player_move---------------------
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

#--------------stop_move and remove key------------------------
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

#============================ KEY EVENT ============================
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)
#============================ WIN & LOSE ============================


#============================ KEY EVENT ============================
canvas.tag_bind("start","<Button-1>", start)
canvas.tag_bind("help","<Button-1>",help)
canvas.tag_bind("exit","<Button-1>", exit)
canvas.tag_bind("back_home","<Button-1>",backHome)
# back select hero
canvas.tag_bind("back_player","<Button-1>",backPlayer)
canvas.tag_bind("next","<Button-1>",next)
canvas.tag_bind("player1","<Button-1>",player1)
canvas.tag_bind("player2","<Button-1>",player2)
canvas.tag_bind("player3","<Button-1>",player3)

canvas.tag_bind("back_all_levels","<Button-1>",backTolevel)
canvas.tag_bind("level1","<Button-1>",level1)
canvas.tag_bind("level2","<Button-1>",level2)
canvas.tag_bind("level3","<Button-1>",level3)

#========================= REMOTES =================


home()

#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()