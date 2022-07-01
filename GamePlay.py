import random
from tkinter import *
from tkinter import font
from tkinter import messagebox


ui = Tk()
ui.geometry()
ui.title("TicTacPhilip")
myFont = font.Font(family = 'Times New Roman', size = 28)
buttons = []
count = 0
actual_place_pos = []
enem=[]


#append adds to list
buttons.append(Button(ui,text="   ", font=myFont, padx=43, pady=40, borderwidth=1, bg="light blue", command=lambda:player_place(1, True)))
buttons.append(Button(ui,text="   ", font=myFont, padx=43, pady=40, borderwidth=1, bg="light blue", command=lambda:player_place(2, True)))
buttons.append(Button(ui,text="   ", font=myFont, padx=43, pady=40, borderwidth=1, bg="light blue", command=lambda:player_place(3, True)))
buttons.append(Button(ui,text="   ", font=myFont, padx=43, pady=40, borderwidth=1, bg="light blue", command=lambda:player_place(4, True)))
buttons.append(Button(ui,text="   ", font=myFont, padx=43, pady=40, borderwidth=1, bg="light blue", command=lambda:player_place(5, True)))
buttons.append(Button(ui,text="   ", font=myFont, padx=43, pady=40, borderwidth=1, bg="light blue", command=lambda:player_place(6, True)))
buttons.append(Button(ui,text="   ", font=myFont, padx=43, pady=40, borderwidth=1, bg="light blue", command=lambda:player_place(7, True)))
buttons.append(Button(ui,text="   ", font=myFont, padx=43, pady=40, borderwidth=1, bg="light blue", command=lambda:player_place(8, True)))
buttons.append(Button(ui,text="   ", font=myFont, padx=43, pady=40, borderwidth=1, bg="light blue", command=lambda:player_place(9, True)))


#lists number from 0 to whatever number is last
buttons[0].grid(row=0, column=0)
buttons[1].grid(row=0, column=1)
buttons[2].grid(row=0, column=2)
buttons[3].grid(row=1, column=0)
buttons[4].grid(row=1, column=1)
buttons[5].grid(row=1, column=2)
buttons[6].grid(row=2, column=0)
buttons[7].grid(row=2, column=1)
buttons[8].grid(row=2, column=2)


def player_place(place_pos, is_player):
    global actual_place_pos
    if buttons[place_pos - 1]['text'] == "   ":
        if is_player:
            actual_place_pos.append(place_pos - 1)
            buttons[place_pos - 1].configure(text="X")
            count_update()
            enemy_place()
            win_declare()
        if is_player == False:
            enem.append(place_pos - 1)
            buttons[place_pos - 1].configure(text="O")
            count_update()
            lose_declare()
    else:
        if is_player == False:
            enemy_place()



def count_update():
    global count
    global board_check
    count = 0
    for button in buttons:
        if button['text'] == "X" or button['text'] == "O":
            count += 1


def enemy_place():
    if count !=9:
        fatAsian = random.randint(1,9)
        player_place(fatAsian, False)
    else:
        tie_declare()


def tie_declare():
    tie_label = Label(ui, font = myFont, text='DRAW!')
    if count == 9:
        tie_label.grid(row=4, column=0, columnspan=3)
        

#WHY THE FUCK AM I DOING THIS
def win_declare():
    global actual_place_pos
    global button
    global place_pos
    win_label = Label(ui, text='YOU WON!!!!', font = myFont)
    for button in buttons:
        for pos in actual_place_pos:
            if button['text'] == "X":
                if 0 in actual_place_pos and 1 in actual_place_pos and 2 in actual_place_pos:
                    win_label.grid(row=4, column=0, columnspan=3)
                if 3 in actual_place_pos and 4 in actual_place_pos and 5 in actual_place_pos:
                    win_label.grid(row=4, column=0, columnspan=3)
                if 6 in actual_place_pos and 7 in actual_place_pos and 8 in actual_place_pos:
                    win_label.grid(row=4, column=0, columnspan=3)
                if 0 in actual_place_pos and 3 in actual_place_pos and 6 in actual_place_pos:
                    win_label.grid(row=4, column=0, columnspan=3)
                if 1 in actual_place_pos and 4 in actual_place_pos and 7 in actual_place_pos:
                    win_label.grid(row=4, column=0, columnspan=3)
                if 2 in actual_place_pos and 5 in actual_place_pos and 8 in actual_place_pos:
                    win_label.grid(row=4, column=0, columnspan=3)
                if 0 in actual_place_pos and 4 in actual_place_pos and 8 in actual_place_pos:
                    win_label.grid(row=4, column=0, columnspan=3)
                if 2 in actual_place_pos and 4 in actual_place_pos and 6 in actual_place_pos:
                    win_label.grid(row=4, column=0, columnspan=3)



def lose_declare():
    global actual_place_pos
    global button
    global place_pos
    lose_label = Label(ui, text='YOU LOST :(', font = myFont)
    for button in buttons:
        if button['text'] == "O":
            for pos in enem:
                if 0 in enem and 1 in enem and 2 in enem:
                    lose_label.grid(row=4, column=0, columnspan=3)
                if 3 in enem and 4 in enem and 5 in enem:
                    lose_label.grid(row=4, column=0, columnspan=3)
                if 6 in enem and 7 in enem and 8 in enem:
                    lose_label.grid(row=4, column=0, columnspan=3)
                if 0 in enem and 3 in enem and 6 in enem:    
                    lose_label.grid(row=4, column=0, columnspan=3)
                if 1 in enem and 4 in enem and 7 in enem:   
                    lose_label.grid(row=4, column=0, columnspan=3)
                if 2 in enem and 5 in enem and 8 in enem:
                    lose_label.grid(row=4, column=0, columnspan=3)
                if 0 in enem and 4 in enem and 8 in enem:
                    lose_label.grid(row=4, column=0, columnspan=3)
                if 2 in enem and 4 in enem and 6 in enem:
                    lose_label.grid(row=4, column=0, columnspan=3)



ui.mainloop()

