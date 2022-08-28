from tkinter import Tk, Label, Entry, Button


root = Tk()
root.geometry("300x300")
root.title("Converter km to miles")
root.resizable(width=False, height=False)

def convert():
    try:
        x = float(int(ent1.get()) * 0.62137)
        mph.config(text=x)
    except:
        mph.config(text="ERROR")

lb1 = Label(root, text=f"Converter from \nkilometers to miles", font=("Arial", 22))
lb1.pack()

ent1 = Entry(root, font=("Arial", 18))
ent1.place(x=80, y=80, height=30, width=140)
lblkm = Label(root, text="KM:", font=("Arial", 16))
lblkm.place(x=30, y=80)

btn1 = Button(root, text="Convert", font=("Arial", 16), command=convert)
btn1.place(x=100, y=120)

mph = Label(root, font=("Arial", 24))
mph.place(x=100, y=180)

lblMph = Label(root, text="MPH:", font=("Arial", 22))
lblMph.place(x=20, y=180)

root.mainloop()