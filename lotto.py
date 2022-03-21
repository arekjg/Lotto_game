from tkinter import *
import time, random
from tkinter.ttk import Progressbar

def button_press(i):
    # choosing numbers and appending to a list
    if len(chosen_list) < 6 and i not in chosen_list:
        global chosen_text
        chosen_text = chosen_text + str(i) + "     "
        chosen_label.set(chosen_text)
        chosen_list.append(i)
    else:
        pass
    return

def clear():
    global chosen_text
    chosen_list.clear()
    chosen_label.set("")
    chosen_text = ""
    drawn_list.clear()
    drawn_label.set("")
    bar["value"] = 0
    lotto_label.set("")  

def draw_numbers():
    # progress bar
    bar["value"] = 0
    a = 50
    b = 0
    speed = 2
    while(b<a):
        time.sleep(0.05)
        bar["value"]+=(speed/a)*100
        b += speed
        window.update_idletasks()
    # drawing random numbers
    drawn_list = random.sample(range(1,50), k=6)
    drawn_text = str(drawn_list[0]) + "     " + str(drawn_list[1]) + "     " + str(drawn_list[2]) + "     " + str(drawn_list[3]) + "     " + str(drawn_list[4]) + "     " + str(drawn_list[5])
    drawn_label.set(drawn_text)
    # comparing list of random numbers with list of chosen numbers
    common = [i for i in drawn_list if i in chosen_list]
    global lotto_result
    # results
    if len(common) == 0:
        lotto_result = "Mishit!"
    elif len(common) == 1:
        lotto_result =  "1 hit!"
    elif len(common) > 1 and len(common) < 5:
        lotto_result = str(len(common)) + " hits!"
    elif len(common) == 5:
        lotto_result = "5 hits! Congratulations!"
    else:
        lotto_result = "You hit 6! YOU WON!"
    lotto_label.set(lotto_result)

# ----------------------------

window = Tk()
window.title("Lotto")
window.geometry("450x500")
window.resizable(False, False)

B_HEIGHT = 1
B_WIDTH = 3
B_FONT = ("Arial Black", 10)

chosen_text = ""
chosen_label = StringVar()
chosen_list = []
drawn_label = StringVar()
drawn_list = []
lotto_label = StringVar()
lotto_result = ""

label1 = Label(window, text = "CHOOSE 6 NUMBERS", font = B_FONT)
label1.pack(pady=15)

frame = Frame(window)
frame.pack()

numbers_list = [*range(1,50)]
for i in numbers_list:
    b = Button(frame, text=i, height=B_HEIGHT, width=B_WIDTH, font=B_FONT, command = lambda i=i: button_press(i))
    if i <= 10:
        b.grid(column=i, row=0)
    elif i > 10 and i <=20:        
        b.grid(column=i-10, row=1)
    elif i > 20 and i <=30:        
        b.grid(column=i-20, row=2)
    elif i > 30 and i <=40:        
        b.grid(column=i-30, row=3)
    else:
        b.grid(column=i-40, row=4)

clear_button = Button(window, text = "CLEAR", height=B_HEIGHT, width=3*B_WIDTH, font=B_FONT, command = clear)
clear_button.pack(pady=10)

label1 = Label(window, text = "YOUR NUMBERS ARE:", font = B_FONT)
label1.pack(pady=10)

labelNums = Label(window, textvariable = chosen_label, font=B_FONT, height=1)
labelNums.pack()

draw_button = Button(window, text = "DRAW", height=B_HEIGHT, width=3*B_WIDTH, font=B_FONT, command = draw_numbers)
draw_button.pack(pady=10)

bar = Progressbar(window, orient=HORIZONTAL, length=200)
bar.pack()

labelR = Label(window, text = "DRAWN NUMBERS: ", font = B_FONT)
labelR.pack()

labelRan = Label(window, textvariable = drawn_label, font=B_FONT, height=1)
labelRan.pack()

resultLabel = Label(window, textvariable = lotto_label, font=B_FONT, height=1)
resultLabel.pack()

window.mainloop()