#============================ IMPORTS ============================
import tkinter as tk
from tkinter import * 
from PIL import ImageTk, Image

#============================ CONSTANTS ============================

WINDOW_WIDTH=1420
WINDOW_HEIGHT=800

GRAVITY_FORCE = 10
JUMP_FORCE = 35
SPEED = 7
TIMED_LOOP = 6


keyPressed = []
#============================ GLOBAL ============================
score=0
isRun = False
isKey = False
#============================ MAIN WINDOW ============================
window = tk.Tk()
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
window.title("KING OF MONKEY")
frame = tk.Frame()
canvas = tk.Canvas(frame,scrollregion= (0,0,4000,5000))


#============================ IMAGES ============================
                #=======BACK GROUND=============
home_bg = PhotoImage(file='Images/bg_home.png')
bg=PhotoImage(file="Images/bg_choose-hero.png")
bg_level=PhotoImage(file="Images/bg_level.png")
bg_level1=PhotoImage(file="Images/level1.png")
bg_level2=PhotoImage(file="Images/level2.png")
bg_level3=PhotoImage(file="Images/level3.png")
bg_lose=PhotoImage(file="Images/bg_lose.png")
bg_level3=PhotoImage(file="Images/bg_level3.png")
winter_bg=PhotoImage(file="Images/winter_bg.png")

                #=======PLAYER IMAGES===========
player1_img=PhotoImage(file="Images/player1.png")
smallplayer1_img=PhotoImage(file="Images/player1_copy.png")
player2_img=PhotoImage(file="Images/player2.png")
player3_img=PhotoImage(file="Images/player3.png")
player = ''

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
ground_wall_level3=PhotoImage(file="Images/ground.png")
land_image=PhotoImage(file="Images/land.png")
grass1_img=PhotoImage(file="Images/grass1.png")


small_grass=PhotoImage(file="Images/grass_L2.png")
stone_img=PhotoImage(file="Images/stone.png")
key_img = PhotoImage(file="Images/key.png")
door_img= PhotoImage(file="Images/door_img.png")
dengerous_land=PhotoImage(file="Images/land_have_enermy.png")
banana_img=PhotoImage(file="Images/banana.png")
lose_img=PhotoImage(file="Images/lose.png")


                #=====ENERMY IMAGES ==========
fire_img=PhotoImage(file="Images/fire.png")
snake_img=PhotoImage(file="Images/snake_img.png")
sea_imgs=PhotoImage(file="Images/sea.png")
# fire_img=PhotoImage(file="Images/fire.png")
# key_img = PhotoImage(file="Images/key.png")

# banana_img=PhotoImage(file="Images/banana.png")
trap_img=PhotoImage(file="Images/trap.png")
# snake_img=PhotoImage(file="Images/snake.png")
# door_img=PhotoImage(file="Images/door.png")
help1_img=PhotoImage(file="Images/help1.png")

# ===========scroll==============
def scroll_bg_img():
    canvas.move('all',-5,0)
    
    if canvas.coords('all')[0]<-5000:
        canvas.coords('all',5000,0)

def scroll_bg_img_1():
    canvas.move('all',5,0)

    if canvas.coords('all')[0]<-5000:
        canvas.coords('all',5000,0)



#=========================== ALL LEVELS =======================





def level1(event):
    global canvas_bg_level1 , player_id, score_id 
    
    # Auto-scrolling--------------------
    scrollbar_bottom = Scrollbar(window, orient='horizontal', command=canvas.xview)
    canvas.configure(xscrollcommand=scrollbar_bottom.set)
    scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')
    #====================score================
    score_id = canvas.create_text(1200, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    
    canvas.delete("all")
    
    #============================= BACKGROUND =====================
    canvas_bg_level1 = canvas.create_image(0,0,image=bg_level1, anchor="nw")
    canvas_bg_level1 = canvas.create_image(1200,0,image=bg_level1, anchor="nw")
    canvas_bg_level1 = canvas.create_image(2400,0,image=bg_level1, anchor="nw")
    canvas_bg_level1 = canvas.create_image(3540,0,image=bg_level1, anchor="nw")
    
    #============= LAND IMAGES =============
    
    canvas.create_image(850,400, image = stone_img, anchor="nw", tags = "plateform")
    canvas.create_image(1220,400, image = stone_img, anchor="nw", tags = "plateform")
    canvas.create_image(2970,400, image = stone_img, anchor="nw", tags = "plateform")
    canvas.create_image(3200,450, image = stone_img, anchor="nw", tags = "plateform")
    canvas.create_image(3280,450, image = stone_img, anchor="nw", tags = "plateform")
    canvas.create_image(3360,450, image = stone_img, anchor="nw", tags = "plateform")
    canvas.create_image(3420,450, image = stone_img, anchor="nw", tags = "plateform")
    #============= STONE IMAGES =============
    canvas.create_image(850,400, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(650,350, image = stone_img, anchor="nw", tags = "platform")
    
    #============ ANERMY IMAGES ==============
    canvas.create_image(400,480,image=fire_img, anchor="nw", tags="anermy")
    canvas.create_image(1000,370,image=fire_img, anchor="nw", tags="anermy")
    canvas.create_image(1600,500,image=fire_img, anchor="nw", tags="anermy")
    canvas.create_image(1400,510,image=snake_img,anchor="nw",tags="anermy")
    canvas.create_image(2000,550,image=fire_img,anchor="nw",tags="anermy")
    canvas.create_image(2600,430,image=snake_img,anchor="nw",tags="anermy")
    canvas.create_image(3350,380,image=snake_img,anchor="nw",tags="anermy")
    #============ FRUIT IMAGES ===============
    canvas.create_image(680,550,image=banana_img,tags="score")
    canvas.create_image(890,400,image=banana_img,tags="score")
    canvas.create_image(1270,390,image=banana_img,tags="score")
    canvas.create_image(1450,480,image=banana_img,tags="score")
    canvas.create_image(1800,570,image=banana_img,tags="score")
    canvas.create_image(2180,580,image=banana_img,tags="score")
    canvas.create_image(2500,500,image=banana_img,tags="score")
    canvas.create_image(3010,400,image=banana_img,tags="score")
    canvas.create_image(3300,430,image=banana_img,tags="score")
    canvas.create_image(3750,580,image=banana_img,tags="score")
    canvas.create_image(950,400,image=banana_img,tags="score")

    #============= UNDER GROUND ============
    canvas.create_image(-50,600,image=ground_wall, anchor="nw", tags="plateform")
    canvas.create_image(350,600,image=ground_wall, anchor="nw", tags="plateform")
    canvas.create_image(1370,600,image=dengerous_land,anchor="nw",tags="plateform")
    canvas.create_image(1650,600,image=dengerous_land,anchor="nw",tags="plateform")
    canvas.create_image(2100,600,image=dengerous_land,anchor="nw",tags="plateform")
    canvas.create_image(2300,600,image=dengerous_land,anchor="nw",tags="plateform")
    canvas.create_image(2500,600,image=dengerous_land,anchor="nw",tags="plateform")
    canvas.create_image(2250,510,image=ground_wall,anchor="nw",tags="plateform")
    canvas.create_image(3600,600,image=dengerous_land,anchor="nw",tags="plateform")
    canvas.create_image(3700,600,image=dengerous_land,anchor="nw",tags="plateform")
    
    #============= KEY ========================
    canvas.create_image(3470,420,image=key_img ,anchor="nw",tags="key")
    
    #============ DOOR =======================
    canvas.create_image(3870,400,image=door_img,anchor="nw",tags="door")
    
    #============= BACK SIGN ===============
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels") 
    
    player_id=canvas.create_image(10,250, image =player, anchor="nw",tags="players1")
    
    score_id = canvas.create_text(1200, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    window.after(TIMED_LOOP, gravity)









    #============ LEVEL TWO ===============
def level2(event):
    global canvas_bg_level2 , player_id, score_id 
    
    canvas.delete("all")
    # canvas.create_image(1, 0, image=bg_level2, anchor="nw")
    #============================= BACKGROUND =====================
    canvas_bg_level2 = canvas.create_image(0,0,image=bg_level2,anchor="nw")
    canvas_bg_level2 = canvas.create_image(1340,0,image=bg_level2,anchor="nw")
    canvas_bg_level2 = canvas.create_image(2400,0,image=bg_level2,anchor="nw")
    canvas_bg_level2 = canvas.create_image(3540,0,image=bg_level2,anchor="nw")

    # Auto-scrolling--------------------
    scrollbar_bottom = Scrollbar(window, orient='horizontal', command=canvas.xview)
    canvas.configure(xscrollcommand=scrollbar_bottom.set)
    scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')
    
    #============= LAND IMAGES =============
    canvas.create_image(100,500, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(1250,550, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(100,100, image = small_grass, anchor="nw", tags = "platform")
    canvas.create_image(350,400, image = small_grass, anchor="nw", tags = "platform")
    canvas.create_image(500,300, image = small_grass, anchor="nw", tags = "platform")
    canvas.create_image(900,500, image = small_grass, anchor="nw", tags = "platform")
    canvas.create_image(700,150, image = small_grass, anchor="nw", tags = "platform")
    canvas.create_image(1100,250, image = small_grass, anchor="nw", tags = "platform")

    canvas.create_image(1650,500, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(1650,100, image = small_grass, anchor="nw", tags = "platform")
    canvas.create_image(2800,550, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(1900,400, image = small_grass, anchor="nw", tags = "platform")
    canvas.create_image(2050,300, image = small_grass, anchor="nw", tags = "platform")
    canvas.create_image(2250,150, image = small_grass, anchor="nw", tags = "platform")
    canvas.create_image(2450,500, image = small_grass, anchor="nw", tags = "platform")
    canvas.create_image(2650,250, image = small_grass, anchor="nw", tags = "platform")
    canvas.create_image(2800,550, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(3000,550, image = small_grass, anchor="nw", tags = "platform")
  
    #============ ANERMY IMAGES ==============
    canvas.create_image(400,490,image=fire_img, anchor="nw", tags="anermy")
    canvas.create_image(1100,490,image=fire_img, anchor="nw", tags="anermy")
    canvas.create_image(1950,490,image=fire_img, anchor="nw", tags="anermy")
    canvas.create_image(2650,490,image=fire_img, anchor="nw", tags="anermy")

    #============ FRUIT IMAGES ===============
    canvas.create_image(200,90,image=banana_img,tags="score")
    canvas.create_image(300,590,image=banana_img,tags="score")
    canvas.create_image(680,590,image=banana_img,tags="score")
    canvas.create_image(750,590,image=banana_img,tags="score")
    canvas.create_image(790,140,image=banana_img,tags="score")
    canvas.create_image(950,400,image=banana_img,tags="score")
    canvas.create_image(1750,80,image=banana_img,tags="score")
    canvas.create_image(2230,590,image=banana_img,tags="score")
    canvas.create_image(2300,590,image=banana_img,tags="score")
    canvas.create_image(2340,140,image=banana_img,tags="score")
    canvas.create_image(2500,485,image=banana_img,tags="score")
    canvas.create_image(2830,550,image=banana_img,tags="score")
    canvas.create_image(3050,540,image=banana_img,tags="score")
    canvas.create_image(3350,540,image=banana_img,tags="score")

    #============= UNDER GROUND ============
    canvas.create_image(-50,600,image=ground_wall, anchor="nw", tags="plateform")
    canvas.create_image(350,600,image=ground_wall, anchor="nw", tags="plateform")
    canvas.create_image(1000,600,image=ground_wall, anchor="nw", tags="plateform")
    canvas.create_image(2050,600,image=ground_wall, anchor="nw", tags="plateform")
    canvas.create_image(3050,600,image=ground_wall, anchor="nw", tags="plateform")
    
    #============ SEA UNDER GROUND ====================
    canvas.create_image(900,630,image=sea_imgs, anchor="nw", tags="plateform")
    canvas.create_image(1540,630,image=sea_imgs, anchor="nw", tags="plateform")
    canvas.create_image(1760,630,image=sea_imgs, anchor="nw", tags="plateform")
    canvas.create_image(1970,630,image=sea_imgs, anchor="nw", tags="plateform")
    canvas.create_image(2530,630,image=sea_imgs, anchor="nw", tags="plateform")
    canvas.create_image(2730,630,image=sea_imgs, anchor="nw", tags="plateform")
    canvas.create_image(2900,630,image=sea_imgs, anchor="nw", tags="plateform")
    canvas.create_image(3600,630,image=sea_imgs, anchor="nw", tags="plateform")
    canvas.create_image(3800,630,image=sea_imgs, anchor="nw", tags="plateform")

    #============= BACK SIGN ===============
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")
    
    player_id=canvas.create_image(10,250, image =player, anchor="nw",tags="players1")
    
    score_id = canvas.create_text(1200, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    window.after(TIMED_LOOP, gravity)







def level3(event):
    global canvas_bg_level3 , player_id, score_id 
    canvas.delete("all")
    # canvas.create_image(1, 0, image=bg_level3, anchor="nw")
    # canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")

#======================= ADD AUTOSCROLLING-BAR ================================
                #=========== BACKGROUND =====================
    canvas_bg_level3 = canvas.create_image(0,0,image=bg_level3,anchor=NW)
    canvas_bg_level3 = canvas.create_image(1340,0,image=bg_level3,anchor=NW)
    canvas_bg_level3 = canvas.create_image(2400,0,image=bg_level3,anchor=NW)
    canvas_bg_level3 = canvas.create_image(3540,0,image=bg_level3,anchor=NW)
                #=========== Auto-scrolling ========================
    scrollbar_bottom = Scrollbar(window, orient='horizontal', command=canvas.xview)
    canvas.configure(xscrollcommand=scrollbar_bottom.set)
    scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

#======================= ADD IMAGE IM LEVEL3 GAME ================================
    #============= STONE IMAGES =============
    canvas.create_image(110,330, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(150,100, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(390,220, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(650,300, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(690,80, image = grass1_img, anchor="nw", tags = "plateform")

    canvas.create_image(950,300, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(1150,100, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(1320,250, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(1650,300, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(1690,80, image = grass1_img, anchor="nw", tags = "plateform")

    canvas.create_image(1950,300, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(2150,100, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(2320,250, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(2650,300, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(2690,80, image = grass1_img, anchor="nw", tags = "plateform")
    
    canvas.create_image(3000,300, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(3140,100, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(3310,370, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(3640,300, image = grass1_img, anchor="nw", tags = "plateform")
    canvas.create_image(3470,100, image = grass1_img, anchor="nw", tags = "plateform")
   
    canvas.create_image(3800,50, image = grass1_img, anchor="nw", tags = "plateform")
    
    #============ ANERMY IMAGES (LOSING WHEN TOUCH ANERMY)==============
    canvas.create_image(340,510,image=fire_img, anchor="nw", tags="anermy")
    canvas.create_image(760,510,image=fire_img, anchor="nw", tags="anermy")
    canvas.create_image(830,510,image=fire_img, anchor="nw", tags="anermy")
    canvas.create_image(2810,510,image=fire_img, anchor="nw", tags="anermy")
    canvas.create_image(3900,460,image=fire_img, anchor="nw", tags="anermy")
    canvas.create_image(3300,460,image=fire_img, anchor="nw", tags="anermy")

    canvas.create_image(230,390,image=trap_img,tags="anermy")
    canvas.create_image(530,280,image=trap_img,tags="anermy")

    #============ FRUIT IMAGES ===============
    canvas.create_image(690,350,image=banana_img,tags="score")
    canvas.create_image(745,350,image=banana_img,tags="score")
    canvas.create_image(800,350,image=banana_img,tags="score")
    
    canvas.create_image(740,130,image=banana_img,tags="score")
    canvas.create_image(795,130,image=banana_img,tags="score")
    canvas.create_image(850,130,image=banana_img,tags="score")
    
    canvas.create_image(200,150,image=banana_img,tags="score")
    canvas.create_image(255,150,image=banana_img,tags="score")
    canvas.create_image(305,150,image=banana_img,tags="score")

    canvas.create_image(100,580,image=banana_img,tags="score")
    canvas.create_image(150,580,image=banana_img,tags="score")
    canvas.create_image(200,580,image=banana_img,tags="score")
    canvas.create_image(250,580,image=banana_img,tags="score")
    canvas.create_image(300,580,image=banana_img,tags="score")
    
    canvas.create_image(470,580,image=banana_img,tags="score")
    canvas.create_image(520,580,image=banana_img,tags="score")
    canvas.create_image(570,580,image=banana_img,tags="score")
    canvas.create_image(620,580,image=banana_img,tags="score")
    canvas.create_image(670,580,image=banana_img,tags="score")
    canvas.create_image(720,580,image=banana_img,tags="score")

    canvas.create_image(150,380,image=banana_img,tags="score")
    canvas.create_image(190,380,image=banana_img,tags="score")

    canvas.create_image(450,280,image=banana_img,tags="score")
    canvas.create_image(490,280,image=banana_img,tags="score")

    canvas.create_image(990,350,image=banana_img,tags="score")
    canvas.create_image(1030,350,image=banana_img,tags="score")
    canvas.create_image(1070,350,image=banana_img,tags="score")

    canvas.create_image(1040,580,image=snake_img,tags="anermy")
    canvas.create_image(1090,580,image=banana_img,tags="score")
    canvas.create_image(1140,580,image=banana_img,tags="score")
    canvas.create_image(1190,580,image=banana_img,tags="score")
    canvas.create_image(1240,580,image=banana_img,tags="score")
    canvas.create_image(1290,580,image=banana_img,tags="score")
    canvas.create_image(1340,580,image=banana_img,tags="score")
    canvas.create_image(1390,580,image=snake_img,tags="anermy")
    canvas.create_image(1440,580,image=snake_img,tags="anermy")
    canvas.create_image(1490,580,image=banana_img,tags="score")
    canvas.create_image(1540,580,image=banana_img,tags="score")
    canvas.create_image(1590,580,image=banana_img,tags="score")
    canvas.create_image(1640,580,image=banana_img,tags="score")
    canvas.create_image(1690,580,image=banana_img,tags="score")
    canvas.create_image(1690,580,image=banana_img,tags="score")
    canvas.create_image(1780,530,image=fire_img,tags="anermy")
    canvas.create_image(1860,580,image=banana_img,tags="score")
    canvas.create_image(1910,580,image=banana_img,tags="score")
    canvas.create_image(1960,580,image=trap_img,tags="anermy")
    canvas.create_image(2010,580,image=banana_img,tags="score")
    canvas.create_image(2070,580,image=banana_img,tags="score")
    canvas.create_image(2120,580,image=banana_img,tags="score")
    canvas.create_image(2170,580,image=trap_img,tags="anermy")
    canvas.create_image(2220,580,image=banana_img,tags="score")
    canvas.create_image(2280,580,image=banana_img,tags="score")
    canvas.create_image(2340,530,image=fire_img,tags="anermy")
    canvas.create_image(2390,580,image=banana_img,tags="score")
    canvas.create_image(2440,580,image=banana_img,tags="score")
    canvas.create_image(2490,580,image=banana_img,tags="score")
    canvas.create_image(2540,580,image=banana_img,tags="score")
    canvas.create_image(2590,580,image=banana_img,tags="score")
    canvas.create_image(2650,580,image=snake_img,tags="anermy")
    canvas.create_image(2710,580,image=banana_img,tags="score")

    canvas.create_image(1200,150,image=banana_img,tags="score")
    canvas.create_image(1250,150,image=banana_img,tags="score")
    canvas.create_image(1300,150,image=banana_img,tags="score")

    canvas.create_image(3880,90, image=banana_img,tags="score")
    canvas.create_image(3930,90, image=door_img, tags = "")

    canvas.create_image(2730,350, image=banana_img, tags = "score")
    canvas.create_image(2780,350, image=key_img, tags = "")
    
    canvas.create_image(1370,300,image=banana_img,tags="score")
    canvas.create_image(1420,300,image=banana_img,tags="score")
    canvas.create_image(1460,300,image=trap_img,tags="anermy")

    canvas.create_image(1370,300,image=banana_img,tags="score")
    canvas.create_image(1420,300,image=banana_img,tags="score")
    canvas.create_image(1460,300,image=trap_img,tags="anermy")

    canvas.create_image(1700,350,image=banana_img,tags="score")
    canvas.create_image(1750,350,image=banana_img,tags="score")
    canvas.create_image(1800,350,image=banana_img,tags="score")

    canvas.create_image(1740,120,image=banana_img,tags="score")
    canvas.create_image(1780,120,image=banana_img,tags="score")
    canvas.create_image(1840,120,image=snake_img,tags="anermy")

    canvas.create_image(2030,350,image=banana_img,tags="score")

    canvas.create_image(2250,150,image=banana_img,tags="score")

    canvas.create_image(2420,290,image=banana_img,tags="score")

    canvas.create_image(3100,350,image=banana_img,tags="score")

    canvas.create_image(3240,150,image=banana_img,tags="score")

    canvas.create_image(3410,420,image=banana_img,tags="score")

    canvas.create_image(3740,350,image=banana_img,tags="score")

    canvas.create_image(3570,150,image=banana_img,tags="score")

    canvas.create_image(2790,130,image=banana_img,tags="score")

    canvas.create_image(2940,580,image=trap_img,tags="anermy")
    canvas.create_image(2990,580,image=banana_img,tags="score")
    canvas.create_image(3040,580,image=banana_img,tags="score")
    canvas.create_image(3090,580,image=banana_img,tags="score")
    canvas.create_image(3140,580,image=trap_img,tags="anermy")
    canvas.create_image(3190,580,image=banana_img,tags="score")
    canvas.create_image(3240,580,image=banana_img,tags="score")
    canvas.create_image(3240,580,image=banana_img,tags="score")

    canvas.create_image(3420,580,image=trap_img,tags="anermy")
    canvas.create_image(3470,580,image=banana_img,tags="score")
    canvas.create_image(3520,580,image=banana_img,tags="score")
    canvas.create_image(3570,580,image=banana_img,tags="score")
    canvas.create_image(3630,580,image=snake_img,tags="anermy")
    canvas.create_image(3680,580,image=banana_img,tags="score")
    canvas.create_image(3730,580,image=banana_img,tags="score")
    canvas.create_image(3780,580,image=banana_img,tags="score")
    canvas.create_image(3830,580,image=trap_img,tags="anermy")
    canvas.create_image(3880,580,image=banana_img,tags="score")

    #============= UNDER GROUND ============
    canvas.create_image(80,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(240,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(510,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(670,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(990,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(1150,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(1310,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(1470,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(1600,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(1760,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(1920,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(2080,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(2240,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(2400,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(2560,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(2720,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(2970,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(3130,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(3290,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(3450,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(3610,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(3770,620,image=ground_wall_level3,tags="plateform")
    canvas.create_image(3930,620,image=ground_wall_level3,tags="plateform")
    
    #============= BACK SIGN ===============
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")
    
    player_id=canvas.create_image(10,250, image =player, anchor="nw",tags="players1")
    
    score_id = canvas.create_text(1200, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    window.after(TIMED_LOOP, gravity)

#============================ SELECT PLAYER ============================
def selectPlayer():
    canvas.delete("all")
    # canvas.create_image(0, 1, image=bg, anchor="nw")
    canvas.create_image(0,0, image=bg, anchor="nw")
    canvas.create_text(720, 100, text="CHOOSE PLAYER", font=("Halloween Slime", 70, "bold"),fill="brown")
                            #==== BACK HOME =====
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
                            #==== PLAYER 1 =====
    canvas.create_image(320, 220, image=player1_img, anchor="nw", tags="player1")
    canvas.create_image(350, 450, image=bord_name, anchor="nw", tags="player1")
    canvas.create_text(440, 485, text="Eli Na", font=("airal", 25, "bold"), fill="#8D4004",tags="player1")
                            #==== PLAYER 2 =====
    canvas.create_image(620, 220, image=player2_img, anchor="nw", tags="player2")
    canvas.create_image(650, 450, image=bord_name, anchor="nw", tags="player2")
    canvas.create_text(740, 485, text="NA RITH", font=("airal", 25, "bold"), fill="#8D4004",tags="player2")
                            # ==== PLAYER 3 =====
    canvas.create_image(920, 220, image=player3_img, anchor="nw", tags="player3")
    canvas.create_image(950, 450, image=bord_name, anchor="nw", tags="player3")
    canvas.create_text(1040, 485, text="SANOK", font=("halloween", 25, "bold"), fill="#8D4004",tags="player3")
    
                            #==== NEXT =====

#PLAYER 1  
def player1(event):
    global player
    canvas.delete("all")
    # player=PLAYER1_CELL
    selectPlayer()
    canvas.create_image(390, 500, image=check, anchor="nw")
    canvas.create_image(1260, 610, image=next_img, anchor="nw", tags="next")
    player=smallplayer1_img
 
#PLAYER 2  
def player2(event):
    global player
    canvas.delete("all")
    selectPlayer()
    canvas.create_image(690, 500, image=check, anchor="nw")
    canvas.create_image(1260, 610, image=next_img, anchor="nw", tags="next")
    player=player2_img

#PLAYER 3
def player3(event):
    global player
    canvas.delete("all")
    selectPlayer()
    canvas.create_image(990, 500, image=check, anchor="nw")
    canvas.create_image(1260, 610, image=next_img, anchor="nw", tags="next")
    player=player3_img

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
    # canvas.create_image(1, 0, image=winter_bg, anchor="nw")
    canvas.create_image(0,0, image = help1_img, anchor="nw")
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
    selectPlayer()
    

#=========================== LOSE AND WIN =======================
def lose():
    canvas.delete("all")
    # Lose_Sound()
    canvas.create_image(1,0, image = bg_lose ,anchor = "nw")
    canvas.create_image(700,350, image = lose_img)
    canvas.create_image(550,550, image = back_img, tags = "backgame")
    score_id = canvas.create_text(750, 474, text=score, font=("arsenal", 25, "bold"), fill="black") 
    canvas.itemconfig(score_id,updatescore)
    
def win():
    if isKey and score > 40:
        canvas.delete("all")
        # Win_Sound()
        canvas.create_image(1,0, image = bg_lose, anchor = "nw")
        # canvas.create_image(700, 350, image = win_img)
        canvas.create_image(550,550, image = back_img, tags = "backgame")
        score_id = canvas.create_text(750, 474, text=score, font=("arsenal", 25, "bold"), fill="black",) 
        canvas.itemconfig(score_id, updatescore)
           
    
#=========================== FUNCTIONS MOVE PLAYER =======================
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player_id)
    platforms = canvas.find_withtag("plateform")
    # if coord[0] + dx < 0 or coord[1] + dx > WINDOW_WIDTH:
    #     return False
    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player.width(), (coord[1] - 50) + player.height() + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]+ player.width() + dx, (coord[1] - 50) + player.height())
    for platform in platforms:
        if platform in overlap:
            return False
    # print()
    return True


def check_movement_enermy():
    coord = canvas.coords(player_id)
    platforms = canvas.find_withtag("anermy")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player.width(), coord[1]+ player.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0


def check_movement_frutis():
    coord = canvas.coords(player_id)
    platforms = canvas.find_withtag("score")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player.width(), coord[1] + player.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0

def check_movement_key():
    coord = canvas.coords(player_id)
    platforms = canvas.find_withtag("key")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player.width(), coord[1] + player.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0

def check_movement_door():
    coord = canvas.coords(player_id)
    platforms = canvas.find_withtag("door")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player.width(), (coord[1]) + player.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0

def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player_id, 0, -force)
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
            
            x -= SPEED
            scroll_bg_img_1()
        if "Right" in keyPressed:
            x += SPEED
            scroll_bg_img()
        if "s" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player_id, x, 0)
            window.after(TIMED_LOOP, move)
    check_more()
#--------check_player_move---------------------
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player_id, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

#--------------stop_move and remove key------------------------
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

def check_more():
    global score, isKey, isRun
    enermy_id = check_movement_enermy()
    fruits_id = check_movement_frutis()
    key_id = check_movement_key()
    door_id = check_movement_door()
    if isRun:
        score = 0
        isRun = False
    if enermy_id > 0:
        # isRun = True
        lose()
    if fruits_id > 0:
        score += 10
        canvas.delete(fruits_id)
        updatescore()
    if key_id >0:
        isKey = True
        canvas.delete(key_id)
    if door_id > 0:
        if isKey==True:
            win()
        else:
            lose()
        
#============================ RESULT SCORE ============================
def updatescore():
    canvas.itemconfig(score_id,text="Score: " + str(score) )
#============================ KEY EVENT ============================
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)


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

canvas.tag_bind("backgame","<Button-1>",backTolevel)
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
