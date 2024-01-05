import tkinter as tk

password = ["→", "↑", "←", "↓"]
input_password = []

def up():
    global password, input_password
    input_password.append("↑")
    label.config(text = input_password)
def left():
    global password, input_password
    input_password.append("←")
    label.config(text = input_password)
def right():
    global password, input_password
    input_password.append("→")
    label.config(text = input_password)
def down():
    global password, input_password
    input_password.append("↓")
    label.config(text = input_password)
def back():
    root_1.destroy()
def check():

    global password, input_password
    if input_password == password:
        root_1.destroy()
    else:
        input_password.clear()


root_1 = tk.Tk()

label = tk.Label(root_1, text = "                          ", font = ("Arial", 20))
label.pack()
#

buttonFrame = tk.Frame(root_1)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

# Buttons


btn1 = tk.Button(buttonFrame, text="Up", font=("Arial", 18), width=10, height=2, command  = up)
btn1.grid(row=0, column=1, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonFrame, text="Left", font=("Arial", 18), width=10, height=2, command = left)
btn2.grid(row=1, column=0, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonFrame, text="Right", font=("Arial", 18), width=10, height=2, command =  right)
btn3.grid(row=1, column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(buttonFrame, text="Down", font=("Arial", 18), width=10, height=2, command = down)
btn4.grid(row=2, column=1, sticky=tk.W+tk.E)
btn5 = tk.Button(buttonFrame, text="Back", font=("Arial", 18), width=10, height=2, command = back)
btn5.grid(row=2, column=0, sticky=tk.W+tk.E)
btn6 = tk.Button(buttonFrame, text="Check", font=("Arial", 18), width=10, height=2, command = check)
btn6.grid(row=2, column=2, sticky=tk.W+tk.E)

buttonFrame.pack(fill='x')

root_1.mainloop()
