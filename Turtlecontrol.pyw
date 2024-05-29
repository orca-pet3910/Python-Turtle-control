from turtle import *
import tkinter as tk

root = tk.Tk()
home()

def fd5():
  fd(5)

def fd25():
  fd(25)

def r5():
  right(5)

def r25():
  right(25)

def l5():
  left(5)

def l25():
  left(25)

btn_f5 = tk.Button(root, text="Forward 5 steps", command=fd5)
btn_f5.pack()
btn_f25 = tk.Button(root, text="Forward 25 steps", command=fd25)
btn_f25.pack()
btn_r5 = tk.Button(root, text="Rotate right 5 degrees", command=r5)
btn_r5.pack()
btn_r25 = tk.Button(root, text="Rotate right 25 degrees", command=r25)
btn_r25.pack()
btn_l5 = tk.Button(root, text="Rotate left 5 degrees" , command=l5)
btn_l5.pack()
btn_l25 = tk.Button(root, text="Rotate left 25 degrees", command=l25)
btn_l25.pack()
btn_ht = tk.Button(root, text="Hide Turtle", command=hideturtle)
btn_ht.pack()
btn_st = tk.Button(root, text="Show Turtle", command=showturtle)
btn_st.pack()
btn_clear = tk.Button(root, text="Clear Screen", command=clear)
btn_clear.pack()
btn_gohome = tk.Button(root, text="Go Home", command=home)
btn_gohome.pack()
btn_undo = tk.Button(root, text="Undo", command=undo)
btn_undo.pack()
root.title("Python Turtle control graphical UI")

root.mainloop()