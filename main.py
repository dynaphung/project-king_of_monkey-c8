#============================ IMPORTS ============================
import tkinter as tk
from tkinter import * 
from PIL import ImageTk, Image

#============================ CONSTANTS ============================

WINDOW_WIDTH=1420
WINDOW_HEIGHT=800

#============================ GLOBAL ============================
score=0


#============================ MAIN WINDOW ============================
window = tk.Tk()
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
window.title("KING OF MONKEY")
frame = tk.Frame()
canvas = tk.Canvas(frame, scrollregion= (0,0,4000,5000))


#============================ IMAGES ============================
                #=======BACK GROUND=============
home_bg = PhotoImage(file='Images/bg_home.png')
bg=PhotoImage(file="Images/bg_choose-hero.png")
bg_level=PhotoImage(file="Images/bg_level.png")
bg_level1=PhotoImage(file="Images/level1.png")
bg_level2=PhotoImage(file="Images/level2.png")
bg_level3=PhotoImage(file="Images/bg_level3.png")
winter_bg=PhotoImage(file="Images/winter_bg.png")

#___________________________________Condition:_____________________________________________
NumberOfLive=0
FoundKey=False
IsWin=False
levels=1

                #=======PLAYER IMAGES===========
player1_img=PhotoImage(file="Images/player1.png")
player2_img=PhotoImage(file="Images/player2.png")
player3_img=PhotoImage(file="Images/player3.png")

#____________________________________monster image____________________________________________________
# monster1_image=tk.PhotoImage(file="image/monster1.png")
# monster1=canvas.create_image(650, 525, image=monster1_image)
monster2_image=tk.PhotoImage(file="Images/monster2.png")
monster2=canvas.create_image(400,435,image=monster2_image)
# monster3_image=tk.PhotoImage(file="image/monster3.png")
# monster3=canvas.create_image(200, 345, image=monster3_image)
# monster4_image=tk.PhotoImage(file="image/monster4.png")
# monster4=canvas.create_image(600, 255, image=monster4_image)
# monster5_image=tk.PhotoImage(file="image/monster5.png")
# monster5=canvas.create_image(450, 165, image=monster5_image)
# bird_image=tk.PhotoImage(file="image/bird_monster.png")
# bird_monster=canvas.create_image(550, 85, image=bird_image)
monsters=[monster2,10,0]
#___________________________________text_image_____________________________________________

def move_monsters():
    global monsters,NumberOfLive,IsWin,levels,Lose_banner,monster_speed
    if NumberOfLive<3 and IsWin==False:
        for n in range(len(monsters)):
            position=canvas.coords(monsters[n][0])
            monsterX = position[0]
            if monsterX<=50 or monsterX>=650:
                monsters[n][1] = -monsters[n][1]
            canvas.move(monsters[n][0],monsters[n][1],monsters[n][2])
            if (canvas.coords(monsters[n][0])[0]-50==canvas.coords(player)[0]+30 and canvas.coords(monsters[n][0])[1]==canvas.coords(player)[1]):
                canvas.moveto(player,0,580)
                NumberOfLive+=1
                # sd_touched()
                # count_number_ofLife()
            if (canvas.coords(monsters[n][0])[0]+50==canvas.coords(player)[0]-30 and canvas.coords(monsters[n][0])[1]==canvas.coords(player)[1]):
                canvas.moveto(player,0,580)
                # NumberOfLive+=1
                # sd_touched()
                # count_number_ofLife()
            if canvas.coords(monsters[n][0])[1]==canvas.coords(player)[1] and canvas.coords(player)[0]-30>=canvas.coords(monsters[n][0])[0]-50 and canvas.coords(monsters[n][0])[0]+50>=canvas.coords(player)[0]+30:
                canvas.moveto(player,0,580)
                # NumberOfLive+=1
                # sd_touched()
                # count_number_ofLife()
        canvas.after(monster_speed,move_monsters)
    if NumberOfLive==3:
        canvas.moveto(Lose_banner,220,325)
        # sd_game_over()
        canvas.after(4000,restart_game)
    move_monsters()




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
stone_img=PhotoImage(file="Images/stone.png")
grass1_img=PhotoImage(file="Images/grass1.png")
wall_img=PhotoImage(file="Images/big_stone.png")
fire_img=PhotoImage(file="Images/fire.png")
key_img = PhotoImage(file="Images/key.png")
# snow_bg = PhotoImage(file="Images/snow_bg.png")
ice_stone = PhotoImage(file="Images/ice_stone.png")
ice_thorn = PhotoImage(file="Images/ice_thorn.png")
small_grass = PhotoImage(file="Images/small_grass.png")
sea_imgs = PhotoImage(file="Images/sea1.png")


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

# Auto-scrolling--------------------
scrollbar_bottom = Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')
banana_img=PhotoImage(file="Images/banana.png")
trap_img=PhotoImage(file="Images/trap.png")
snake_img=PhotoImage(file="Images/snake.png")
door_img=PhotoImage(file="Images/door.png")
help1_img=PhotoImage(file="Images/help1.png")

#=========================== ALL LEVELS =======================

def level1(event):
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_level1, anchor="nw")
    
    #============= STONE IMAGES =============
    canvas.create_image(850,400, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(650,350, image = stone_img, anchor="nw", tags = "platform")
    
    #============ ANERMY IMAGES ==============
    canvas.create_image(400,480,image=fire_img, anchor="nw", tags="anermy")
    
    #============ FRUIT IMAGES ===============
    canvas.create_image(680,550,image=banana_img,tags="score")
    canvas.create_image(950,400,image=banana_img,tags="score")

    #============= UNDER GROUND ============
    canvas.create_image(-50,600,image=ground_wall, anchor="nw", tags="plateform")
    canvas.create_image(350,600,image=ground_wall, anchor="nw", tags="plateform")
    
    #============= BACK SIGN ===============
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")
    
    
    
    #============ LEVEL TWO ===============
def level2(event):
    global canvas_bg_level2 , player, score_id
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
    



    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")

def level3(event):
    canvas.delete("all")
    canvas.create_image(1, 0, image=bg_level3, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")

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
    canvas.create_image(90,330, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(150,100, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(390,220, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(650,300, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(690,80, image = grass1_img, anchor="nw", tags = "platform")

    canvas.create_image(950,300, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(1150,100, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(1320,250, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(1650,300, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(1690,80, image = grass1_img, anchor="nw", tags = "platform")

    canvas.create_image(1950,300, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(2150,100, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(2320,250, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(2650,300, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(2690,80, image = grass1_img, anchor="nw", tags = "platform")
    
    canvas.create_image(3000,300, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(3140,100, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(3310,370, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(3640,300, image = grass1_img, anchor="nw", tags = "platform")
    canvas.create_image(3470,100, image = grass1_img, anchor="nw", tags = "platform")
   
    canvas.create_image(3800,50, image = grass1_img, anchor="nw", tags = "platform")
    
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
    canvas.create_text(1040, 485, text="SANOK", font=("airal", 25, "bold"), fill="#8D4004",tags="player3")
    
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
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    selectPlayer()
#=========================== FUNCTIONS MOVE PLAYER =======================
# MOVE RIGHT
def moveRight(event):
    pass
    
# MOVE LEFT
def moveLeft(event):
    pass
    
# MOVE UP
def moveUp(event):
    pass

# MOVE DOWN
def moveDown(event):
    pass 



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
