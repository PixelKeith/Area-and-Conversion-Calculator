import tkinter as tk
import area
import conversion

def change_button_area():
    title.config(text="Area Calculator")

def change_button_unit():
    title.config(text="Unit Converter")

window = tk.Tk()
window.title("Area and Conversion Calculator")
window.config(bg="#1A1A24")
window.geometry("350x500")
window.resizable(False, False)

try:
    icon = tk.PhotoImage(file="logo.png")
    window.iconphoto(True, icon)
except Exception:
    pass

title = tk.Label(
    window,
    text="Area Calculator",
    font=("Courier New", 20, "bold"),
    fg="#E2E8F0",
    bg="#242533",
    relief="ridge",
    width=16,
    bd=7,
    padx=30,
    pady=15
)

title.pack(side="top",pady=(20, 15))

button_area = tk.Button(
    text="Area Calculator",
    command=change_button_area
)
button_area.pack()

button_unit = tk.Button(
    text="Unit Converter",
    command=change_button_unit
)
button_unit.pack(side="right")

window.mainloop()