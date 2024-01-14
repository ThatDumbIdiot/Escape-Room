import tkinter as tk
from tkinter import PhotoImage, Label, messagebox
from pygame import mixer

inventory_c = []
inventory_p = []
password = ["→", "↑", "←", "↓"]
input_password = []

def l():
    global label_4, label_5, label_6, label_7, label_8, label_9, label_10, label_11, label_12
    global label_13, label_14, label_15, label_16, label_17, label_18, label_19, label_20, label_21, label_22, label_24
    global button_map_2, button_map_3, button_map_4
    label_4.place_forget()
    label_5.place_forget()
    label_6.place_forget()
    label_7.place_forget()
    label_8.place_forget()
    label_9.place_forget()
    label_10.place_forget()
    label_11.place_forget()
    label_12.place_forget()
    label_13.place_forget()
    label_14.place_forget()
    label_15.place_forget()
    label_16.place_forget()
    label_17.place_forget()
    label_18.place_forget()
    label_19.place_forget()
    label_20.place_forget()
    label_21.place_forget()
    label_22.place_forget()
    label_24.place_forget()
    button_map_2.pack_forget()
    button_map_3.pack_forget()
    button_map_4.pack_forget()


def toggle_pause():
    if mixer.music.get_busy():
        mixer.music.pause()
        button_music.config(text="Music: Off")
    else:
        mixer.music.unpause()
        button_music.config(text="Music: On")
        
#Typing animation(Dont touch unless Your Chat Gpt)
def type_text(text, label, interval=50, step=1):
    for i in range(0, len(text) + 1, step):
        partial_text = text[:i]
        label.config(text=partial_text)
        root.update()
        root.after(interval)

#Start Screen
def re_start():
    
    back_prison.forget()
    back_down.forget()
    back_forward.forget()
    back_right.forget()
    back_left.forget()
    button_f.place_forget()
    button_l.place_forget()
    button_r.place_forget()
    button_d.place_forget()
    label_inv.place_forget()
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    btn_4.place_forget()
    label_int.place_forget()
    btn_5.place_forget()
    btn_6.place_forget()
    btn_7.place_forget()
    btn_8.place_forget()
    
    
    l()
    root.configure(bg="#333333")
    label_1.pack_forget()
    button_1.pack_forget()

    label_2.pack()
    button_prison.pack()
    button_map_2.pack()
    button_map_3.pack()
    button_map_4.pack()

    button_restart.place(x=10, y=480)
    button_quit.place(x=85, y=480)
    button_music.place(x=205, y=480)

    # Background music
    music_file = "escape_room.mp3"  # Replace with the path to your background music file
    mixer.init()
    mixer.music.load(music_file)
    mixer.music.play(-1)
    
def start():
    label_1.pack_forget()
    button_1.pack_forget()

    label_2.pack()
    button_prison.pack()
    button_map_2.pack()
    button_map_3.pack()
    button_map_4.pack()
    
    button_restart.place(x = 10, y = 480)
    button_quit.place(x = 85, y=480)
    button_music.place(x = 205, y = 480)
    # Background music
    music_file = "escape_room.mp3" 
    mixer.init()
    mixer.music.load(music_file)
    mixer.music.play(-1)

#Quit
def q():
    if messagebox.askyesno("Quit?", "Do you want to quit?"):
        root.destroy()

#Prison Map------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   







        
#Interactions
def int1():
    global inventory_p
    if "wrench" in inventory_p:
        l()
        ###
        text_12 = "You look at the pillow and notice some drawings on them"
        label_14.place(x = 175, y = 10)
        type_text(text_12, label_14)
        ###
        text_13 = "It has a number written on it, 'Time:- 3185'"
        label_15.place(x = 175, y = 50)
        type_text(text_13, label_15)
        ###
        btn_2.config(text = "Time - 3185")
        inventory_p.append("3185")
        btn_5.config(state = tk.DISABLED)
    else:
        l()
        ###
        text_12 = "You look under the bed and notice something shiny"
        label_14.place(x = 175, y = 10)
        type_text(text_12, label_14)
        ###
        text_13 = "You found a Wrench under the bed, it might help you later"
        label_15.place(x = 175, y = 50)
        type_text(text_13, label_15)
        ###
        btn_1.config(text = "wrench")
        inventory_p.append("wrench")
def int2():
    global inventory_p
    if "Nail File" in inventory_p:
        pass
    else:
        l()
        ###
        text_14 = "You moved the brick and found a nail file underneath"
        label_16.place(x=175, y=10)
        type_text(text_14, label_16)
        btn_3.config(text="Nail File")
        btn_6.config(state=tk.DISABLED)
        inventory_p.append("Nail File")

def int3():
    # Puzzle
    global inventory_p, done, password, input_password

    if "wrench" in inventory_p:
        def up():
            input_password.append("↑")
            label.config(text=input_password)

        def left():
            input_password.append("←")
            label.config(text=input_password)

        def right():
            input_password.append("→")
            label.config(text=input_password)

        def down():
            input_password.append("↓")
            label.config(text=input_password)

        def back():
            if input_password:
                input_password.pop()
                label.config(text=input_password)

        def clear():
            input_password.clear()
            label.config(text=input_password)

        def check():
            global inventory_p
            if input_password == password:
                root_1.destroy()
                label_11.place_forget()
                label_12.place_forget()
                text_19 = "You opened the faucet and found a small metal rod"
                label_21.place(x=175, y=10)
                type_text(text_19, label_21)
                btn_4.config(text="Metal Rod")
                inventory_p.append("Metal Rod")
                btn_7.config(state=tk.DISABLED)
            else:
                input_password.clear()

        root_1 = tk.Tk()
        root_1.config(bg = "#301934")
        label = tk.Label(root_1, text="                          ", font=("Arial", 20), bg = "#301934", fg = "white")
        label.grid(row = 0, column = 1)
        

        btn1 = tk.Button(root_1, text="Up", font=("Arial", 18), width=10, height=2, command=up, bg="#8b0000", fg="white")
        btn1.grid(row=1, column=1, sticky=tk.W + tk.E)
        btn2 = tk.Button(root_1, text="Left", font=("Arial", 18), width=10, height=2, command=left, bg="#8b0000", fg="white")
        btn2.grid(row=2, column=0, sticky=tk.W + tk.E)
        btn3 = tk.Button(root_1, text="Right", font=("Arial", 18), width=10, height=2, command=right, bg="#8b0000", fg="white")
        btn3.grid(row=2, column=2, sticky=tk.W + tk.E)
        btn4 = tk.Button(root_1, text="Down", font=("Arial", 18), width=10, height=2, command=down, bg="#8b0000", fg="white")
        btn4.grid(row=3, column=1, sticky=tk.W + tk.E)
        btn5 = tk.Button(root_1, text="Back", font=("Arial", 18), width=10, height=2, command=back, bg="#8b0000", fg="white")
        btn5.grid(row=4, column=0, sticky=tk.W + tk.E)
        btn6 = tk.Button(root_1, text="Clear", font=("Arial", 18), width=10, height=2, command=clear, bg="#8b0000", fg="white")
        btn6.grid(row=4, column=2, sticky=tk.W + tk.E)
        btn7 = tk.Button(root_1, text="Check", font=("Arial", 18), width=10, height=2, command=check, bg="#8b0000", fg="white")
        btn7.grid(row=4, column=1, sticky=tk.W + tk.E)

        

        root_1.mainloop()
    else:
        l()
            
        ###
        text_20 = "Nothings working here"
        label_22.place(x = 175, y = 10)
        type_text(text_20, label_22)
def int4():
    root.destroy()
    root1 = tk.Tk()
    root1.geometry("800x529")
    root1.title("Escape Room")
    root1.config(bg="Black")

    # Display the end screen text
    label_21 = tk.Label(root1, font=("Arial", 16), bg="black", fg="white")
    label_22 = tk.Label(root1, font=("Arial", 16), bg="black", fg="white")
    label_23 = tk.Label(root1, font=("Arial", 16), bg="black", fg="white")

    text_19 = "You Opened the lock and escaped"
    label_21.place(x=250, y=100)
    type_text(text_19, label_21)


    text_20 = "The End"
    label_22.place(x = 350, y=150)
    type_text(text_20, label_22)


    text_21 = "Thanks for playing! More maps coming soon!"
    label_23.place(x=200, y=200)
    type_text(text_21, label_23)


    


#Hints
def P_hint():
    if messagebox.askyesno("Hint", "Would You like a hint?"):
        l()

        text_22 = "Look forward and try inspecting it"
        label_24.place(x = 200, y = 10)
        type_text(text_22, label_24)


    
#Prison Escape
def prison_map():
    l()
    #Loading
    label_2.pack_forget()
    button_prison.pack_forget()

    root.after(100, lambda: label_3.pack(pady=150))

    text_1 = "Loading Map............"
    type_text(text_1, label_3)

    root.after(100, lambda: label_3.pack_forget())
        
    #StoryLine
    back_prison.pack()

    root.after(1, lambda: label_4.place(x = 200, y = 10))

    text_2 = "You have woken up in a dark prison cell"
    type_text(text_2, label_4)

    label_5.place(x = 175, y = 50)
    text_3 = "You have nothing on you but you must escape soon"
    type_text(text_3, label_5)

    label_6.place(x = 250, y = 90)
    text_4 = "Where would you like to look?"
    type_text(text_4, label_6)

    #Interactive Buttons
    button_f.place(x = 350, y = 300)
    button_l.place(x = 275, y = 350)
    button_r.place(x = 445, y = 350)
    button_d.place(x = 350, y = 400)
    button_hint.place(x=145, y=480)

    #Inventory
    label_inv.place(x = 10, y = 90)
    btn_1.place(x = 10, y = 125)
    btn_2.place(x = 10, y = 160)
    btn_3.place(x = 10, y = 195)
    btn_4.place(x = 10, y = 230)
    #Interactive Options
    label_int.place( x = 700, y = 90)
    btn_5.place(x = 700, y = 125)
    btn_6.place(x = 700, y = 170)
    btn_7.place(x = 700, y = 215)
    btn_8.place(x = 700, y = 260)
    
def P_left():
    global inventory_p
    l()
    #
    back_down.place_forget()
    back_right.place_forget()
    back_left.place_forget()
    back_forward.place_forget()
    btn_5.config(state = tk.DISABLED)
    btn_6.config(state = tk.DISABLED)
    btn_7.config(state = tk.DISABLED)
    btn_8.config(state = tk.DISABLED)
    
    ###
    back_left.place(x=0, y=0)
    #
    label_8.place(x=125, y=10)
    text_6 = "You notice a door, You try to open it but realise that it wont budge!"
    type_text(text_6, label_8)
    ###
    label_13.place(x=25, y=50)
    text_11 = "You see that the door has a hole for a key, You think that you could get it open?"
    type_text(text_11, label_13)
    ###
    if "Nail File".lower() in inventory_p and "Metal Rod" in inventory_p:
        btn_8.config(state = tk.NORMAL)
    else:
        pass
def P_forward():
    l()
    #
    back_down.place_forget()
    back_right.place_forget()
    back_left.place_forget()
    back_forward.place_forget()
    btn_5.config(state = tk.DISABLED)
    btn_6.config(state = tk.DISABLED)
    btn_7.config(state = tk.DISABLED)
    btn_8.config(state = tk.DISABLED)
    ###
    back_forward.place(x=0, y=0)
    ###
    label_9.place(x=125, y=10)
    text_7 = "You look forward and notice an old and rusty bed."
    type_text(text_7, label_9)
    ###
    label_10.place(x=125, y=50)
    text_8 = "You also see a window but it has bars along the whole window :("
    type_text(text_8, label_10)
    ###
    btn_5.config(state = tk.NORMAL)
def P_down():
    l()
    #
    back_down.place_forget()
    back_right.place_forget()
    back_left.place_forget()
    back_forward.place_forget()
    btn_5.config(state = tk.DISABLED)
    btn_6.config(state = tk.DISABLED)
    btn_7.config(state = tk.DISABLED)
    btn_8.config(state = tk.DISABLED)

    ###
    back_down.place(x=0, y=0)
    ###
    label_7.place(x=175, y=10)
    text_5 = "You look down and notice a Loose Brick on the Floor"
    type_text(text_5, label_7)
    ###
    btn_6.config(state = tk.NORMAL)
def P_right():
    l()
    #
    back_down.place_forget()
    back_right.place_forget()
    back_left.place_forget()
    back_forward.place_forget()
    btn_5.config(state = tk.DISABLED)
    btn_6.config(state = tk.DISABLED)
    btn_7.config(state = tk.DISABLED)
    btn_8.config(state = tk.DISABLED)
    ###
    back_right.place(x=0, y=0)
    ###
    text_9 = "A sink is present there with the pipes running along"
    label_11.place(x=150, y=10)
    type_text(text_9, label_11)
    ###
    text_10 = "You try to turn on the water but the water isn't running!"
    label_12.place(x=150, y=50)
    type_text(text_10, label_12)
    ###
    btn_7.config(state = tk.NORMAL)
#End of Prison Map--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Start of Office Map------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def office():
    pass
#End of Office Map--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Start of car Map--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def car_front():

    button_restart.place(x = 10, y = 480)
    button_quit.place(x = 85, y=480)
    button_music.place(x = 205, y = 480)
    
    car_forward.pack()
    car_forward_puzzle.place(x = 338, y = 65)
def car_game():
    label_4.place_forget()
    label_5.place_forget()
    label_6.place_forget()
    label_7.place_forget()
    label_8.place_forget()
    label_9.place_forget()
    label_10.place_forget()
    label_11.place_forget()
    label_12.place_forget()
    label_13.place_forget()
    label_14.place_forget()
    label_15.place_forget()
    label_16.place_forget()
    label_17.place_forget()
    label_18.place_forget()
    
    car_front()
    
def story():
    def forget():
        label_4.place_forget()
        label_5.place_forget()
        label_6.place_forget()
        label_7.place_forget()
        label_8.place_forget()
        label_9.place_forget()
        label_10.place_forget()
        label_11.place_forget()
        label_12.place_forget()
        label_13.place_forget()
        label_14.place_forget()
        label_15.place_forget()
        label_16.place_forget()
        label_17.place_forget()
        label_18.place_forget()
    #Slide 1
    img_1.pack()
    text_2 = "Welcome to your challenge!"
    text_3 = "You find yourself standing in front of a mysterious Ford Expedition"
    text_4 = "The engine is running, and the door is unlocked. What awaits you inside?"
    
    label_4.place(x=250, y=10)
    type_text(text_2, label_4)
    label_5.place(x = 125, y = 50)
    type_text(text_3, label_5)
    label_6.place(x = 90, y = 90)
    type_text(text_4, label_6)
    img_1.pack_forget()
    root.after(500, forget())
    #Slide 2
    img_2.pack()
    text_5 = "You step inside and notice the car is impeccably clean"
    text_6 = "The soft hum of the engine and the faint sound of distant traffic fills the air"
    text_7 = "Your escape begins now. Search and solve puzzles to unlock the secrets within."

    
    label_7.place(x = 140, y =10)
    type_text(text_5, label_7)
    label_8.place(x = 80, y = 50)
    type_text(text_6, label_8)
    label_9.place(x = 10, y = 90)
    type_text(text_7, label_9)
    img_2.pack_forget()
    root.after(500, forget())
    #Slide 3
    img_3.pack()
    text_8 = "Opening the glove compartment, you discover a set of keys and a mysterious note."
    text_9 = "The note reads:"
    text_10 = '"The journey begins with a key. Find the right one, and your path will unfold."'
    text_11 = "Take note of every detail; the key to your escape may be hidden in plain sight."

    label_10.place(x = 10, y = 10)
    type_text(text_8, label_10)
    label_11.place(x = 300, y = 50)
    type_text(text_9, label_11)
    label_12.place(x = 50, y = 90)
    type_text(text_10, label_12)
    label_13.place(x = 40, y = 130)
    type_text(text_11, label_13)
    img_3.pack_forget()
    root.after(500, forget())
    #Slide 4
    img_4.pack()
    text_12 = "As you explore the back seat, you notice something unusual tucked inside the cushions"
    text_13 = "What secrets does the rear seat hold? Investigate carefully to reveal hidden clues."

    label_14.place(x = 0, y = 10)
    type_text(text_12, label_14)
    label_15.place(x = 15, y = 50)
    type_text(text_13, label_15)
    img_4.pack_forget()
    root.after(500, forget())
    #Slide 5
    img_5.pack()
    text_14 = "Your attention is drawn to the locked trunk. What mysteries lie behind its confines?"
    text_15 = "Solve the puzzles within the trunk to unlock the next stage of your journey"
    text_16 = "The key you found earlier might come in handy"

    label_16.place(x = 2, y = 10)
    type_text(text_14, label_16)
    label_17.place(x = 10, y = 50)
    type_text(text_15, label_17)
    label_18.place(x = 150, y = 90)
    type_text(text_16, label_18)
    img_5.pack_forget()
    root.after(500, forget())

    car_game()
    
def car():
    l()
    
    label_2.pack_forget()
    button_prison.pack_forget()

    root.after(100, lambda: label_3.pack(pady=150))

    text_1 = "Loading Map............"
    type_text(text_1, label_3)

    root.after(100, lambda: label_3.pack_forget())

    #Storyline
    root.after(1, lambda: story())
#End of Car Map--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Start of School Map-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def headlands():
    pass
#End of School Map--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#GUI
root = tk.Tk()
root.configure(bg="#333333")
root.geometry("800x529")
root.title("Escape Room")

###Start Screen
label_1 = tk.Label(root, text = "Welcome to the Escape Room!!!", font = ("Arial", 30), bg = "#333333", fg = "White")
label_1.pack()

button_1 = tk.Button(root, text = "Start Game", font = ("Arial", 20), bg = "White", fg = "Black", command = start, width = 15, height = 2)
button_1.pack(pady = 150)



#Map options
image = tk.PhotoImage(file='prison.png')
button_prison = tk.Button(root, image=image, width = 200, height = 100, command = prison_map)
button_map_2 = tk.Button(root, text = "In Progress...", font = ("Arial", 20) , width = 15, height = 2, command = car)
button_map_3 = tk.Button(root, text = "Coming Soon...", font = ("Arial", 20) , width = 15, height = 2, command = office)
button_map_4 = tk.Button(root, text = "Coming Soon...", font = ("Arial", 20) , width = 15, height = 2, command = headlands)
label_2 = tk.Label(root, text = "Choose The Map", font = ("Arial", 30), bg = "#333333", fg = "White")

#Prison GUI------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Background
bg_back = PhotoImage(file="prison_1.png")
back_prison = tk.Label(root, image = bg_back)
bg_down = PhotoImage(file="p_down.png")
back_down = tk.Label(root, image=bg_down)
bg_forward = PhotoImage(file = "p_bed.png")
back_forward = tk.Label(root, image = bg_forward)
bg_right = PhotoImage(file = "p_sink.png")
back_right = tk.Label(root, image = bg_right)
bg_left = PhotoImage(file = "p_door.png")
back_left = tk.Label(root, image = bg_left)



#Directional Buttons
button_f = tk.Button(root, text = "Forward", font=("Arial", 16), bg = "#333333", fg = "White", command = P_forward)
button_l = tk.Button(root, text = "  Left  ", font=("Arial", 16), bg = "#333333", fg = "White", command = P_left)
button_r = tk.Button(root, text = " Right ", font=("Arial", 16), bg = "#333333", fg = "White", command = P_right)
button_d = tk.Button(root, text = "  Down  ", font=("Arial", 16), bg = "#333333", fg = "White", command = P_down)


#Inventory
label_inv = tk.Label(root, text = "Inventory", font = ("Arial", 16))
btn_1 = tk.Label(root, text = "             ",  font=("Arial", 16))
btn_2 = tk.Label(root, text = "             ",  font=("Arial", 16))
btn_3 = tk.Label(root, text = "             ",  font=("Arial", 16))
btn_4 = tk.Label(root, text = "             ",  font=("Arial", 16))


#Interactive Options
label_int = tk.Label(root, text = "Options", font = ("Arial", 16))
btn_5 = tk.Button(root, text = "  Inspect  ",  font=("Arial", 16), command = int1, state = tk.DISABLED)
btn_6 = tk.Button(root, text = "  Inspect  ",  font=("Arial", 16), command = int2, state = tk.DISABLED)
btn_7 = tk.Button(root, text = "  Inspect  ",  font=("Arial", 16), command = int3, state = tk.DISABLED)
btn_8 = tk.Button(root, text = "    Use    ",  font=("Arial", 16), command = int4, state = tk.DISABLED)


#End of Prison GUI--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Start of Car GUI---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Images
img1 = tk.PhotoImage(file = 'car_1.png')
img_1 = tk.Label(root, image = img1)
img2 = tk.PhotoImage(file = 'car_2.png')
img_2 = tk.Label(root, image = img2)
img3 = tk.PhotoImage(file = 'car_3.png')
img_3 = tk.Label(root, image = img3)
img4 = tk.PhotoImage(file = 'car_4.png')
img_4 = tk.Label(root, image = img4)
img5 = tk.PhotoImage(file = 'car_5.png')
img_5 = tk.Label(root, image = img5)



#Text Animation
label_3 = tk.Label(root, font= ("Arial", 16), bg = "#333333", fg = "White")
label_4 = tk.Label(root, font= ("Arial", 16), bg = "#333333", fg = "White")
label_5 = tk.Label(root, font= ("Arial", 16), bg = "#333333", fg = "White")
label_6 = tk.Label(root, font= ("Arial", 16), bg = "#333333", fg = "White")
label_7 = tk.Label(root, font= ("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_8 = tk.Label(root, font= ("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_9 = tk.Label(root, font= ("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_10 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_11 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_12 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_13 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_14 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_15 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_16 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_17 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_18 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_19 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_20 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_21 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_22 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")
label_24 = tk.Label(root, font=("Arial", 16), bg = "#d2d6d9", fg = "Black")

#Quit and Hint
button_quit = tk.Button(root, text = "Quit",  font=("Arial", 16), bg = "#333333", fg = "White", command = q)
button_hint = tk.Button(root, text = "Hint",  font=("Arial", 16), bg = "#333333", fg = "White", command = P_hint)
button_music = tk.Button(root, text = "Music: On", font=("Arial", 16), bg = "#333333", fg = "White", command = toggle_pause)
button_restart = tk.Button(root, text = "Home",  font=("Arial", 16), bg = "#333333", fg = "White", command = re_start)

#Puzzle No1
car_fwd = tk.PhotoImage(file='car_6.png')
car_forward = tk.Label(root, image = car_fwd)
car_fwd_puzzle = tk.PhotoImage(file='car_puzzle_6.png')
car_forward_puzzle = tk.Button(root, image=car_fwd_puzzle, bd=0, highlightthickness=0)
car_forward_puzzle.config(highlightbackground=root.cget('bg'))


root.mainloop()


