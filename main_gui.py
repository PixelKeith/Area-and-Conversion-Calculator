from tkinter import *

window = Tk()
window.geometry("400x550")
window.title("Area Calculator and Unit Converter")

icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)
window.config(background= "black")

label = Label(
    window,
    text="Keith's Area Calculator and Unit Converter",
    font=("Segoe UI", 18),
    bg="black",
    fg="white"
)
label.pack(pady=20)

window.mainloop()