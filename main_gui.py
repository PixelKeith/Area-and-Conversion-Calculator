import tkinter as tk
from tkinter import ttk
import area


def change_button_area():
    title.config(text="Area Calculator")
    shape_frame.pack(fill="x", pady=(0, 30))
    update_inputs(None)


def change_button_unit():
    title.config(text="Unit Converter")
    shape_frame.pack_forget()
    hide_input()
    result_label.config(text="Unit Converter Mode Active", fg="#E2E8F0")


def hide_input():
    input1_frame.pack_forget()
    input2_frame.pack_forget()
    input3_frame.pack_forget()
    action_frame.pack_forget()


def update_inputs(event):
    hide_input()
    chosen = shape.get()

    match chosen:
        case "Square":
            label1.config(text="Side:")
            input1_frame.pack(fill="x", pady=(0, 10))
        case "Parallelogram" | "Rectangle" | "Triangle":
            label1.config(text="Base:")
            label2.config(text="Height:")
            input1_frame.pack(fill="x", pady=(0, 10))
            input2_frame.pack(fill="x", pady=(0, 10))
        case "Circle":
            label1.config(text="Radius:")
            input1_frame.pack(fill="x", pady=(0, 10))
        case "Trapezoid":
            label1.config(text="Base 1:")
            label2.config(text="Base 2:")
            label3.config(text="Height:")
            input1_frame.pack(fill="x", pady=(0, 10))
            input2_frame.pack(fill="x", pady=(0, 10))
            input3_frame.pack(fill="x", pady=(0, 10))

    action_frame.pack(fill="x", pady=(15, 0))
    input1.delete(0, tk.END)
    input2.delete(0, tk.END)
    input3.delete(0, tk.END)
    result_label.config(text="")


def run_calculation():
    try:
        chosen = shape.get()
        v1 = float(input1.get()) if input1.get() else 0.0
        v2 = float(input2.get()) if input2.get() else 0.0
        v3 = float(input3.get()) if input3.get() else 0.0

        result = 0.0

        match chosen:
            case "Square":
                result = area.area_square(v1)
            case "Rectangle":
                result = area.area_rectangle(v1, v2)
            case "Parallelogram":
                result = area.area_parallelogram(v1, v2)
            case "Triangle":
                result = area.area_triangle(v1, v2)
            case "Circle":
                result = area.area_circle(v1)
            case "Trapezoid":
                result = area.area_trapezoid(v1, v2, v3)

        if result.is_integer():
            result = int(result)
        else:
            result = round(result, 2)

        result_label.config(text=f"Area = {result}", fg="#00FF00")
    except ValueError:
        result_label.config(text="Invalid inputs!", fg="#FF3333")


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
title.pack(side="top", pady=(20, 15))

button_frame = tk.Frame(window, bg="#1A1A24")
button_frame.pack(pady=(0, 30))

button_area = ttk.Button(
    button_frame,
    text="Area Calculator",
    width=20,
    command=change_button_area
)
button_area.pack(side="left", padx=15)

button_unit = ttk.Button(
    button_frame,
    text="Unit Converter",
    width=20,
    command=change_button_unit
)
button_unit.pack(side="left", padx=15)

shape_frame = tk.Frame(window, bg="#1A1A24")
shape_frame.pack(fill="x", pady=(0, 30))

shape_label = tk.Label(
    shape_frame,
    text="Shape:",
    font=("Courier New", 13, "bold"),
    bg="#1A1A24",
    fg="#E2E8F0",
    width=8,
    anchor="w"
)
shape_label.pack(side="left", padx=(35, 10))

shape = ttk.Combobox(
    shape_frame,
    values=["Square", "Parallelogram", "Rectangle", "Trapezoid", "Triangle", "Circle"],
    state="readonly"
)
shape.pack(side="left")
shape.set("Square")
shape.bind("<<ComboboxSelected>>", update_inputs)

input1_frame = tk.Frame(window, bg="#1A1A24")
label1 = tk.Label(
    input1_frame,
    text="Side:",
    font=("Courier New", 13, "bold"),
    bg="#1A1A24",
    fg="#E2E8F0",
    width=8,
    anchor="w"
)
label1.pack(side="left", padx=(35, 10))
input1 = ttk.Entry(input1_frame, width=20)
input1.pack(side="left")

input2_frame = tk.Frame(window, bg="#1A1A24")
label2 = tk.Label(
    input2_frame,
    text="Side:",
    font=("Courier New", 13, "bold"),
    bg="#1A1A24",
    fg="#E2E8F0",
    width=8,
    anchor="w"
)
label2.pack(side="left", padx=(35, 10))
input2 = ttk.Entry(input2_frame, width=20)
input2.pack(side="left")

input3_frame = tk.Frame(window, bg="#1A1A24")
label3 = tk.Label(
    input3_frame,
    text="Side:",
    font=("Courier New", 13, "bold"),
    bg="#1A1A24",
    fg="#E2E8F0",
    width=8,
    anchor="w"
)
label3.pack(side="left", padx=(35, 10))
input3 = ttk.Entry(input3_frame, width=20)
input3.pack(side="left")


action_frame = tk.Frame(
    window,
    bg="#1A1A24"
)

calc_button = ttk.Button(
    action_frame,
    text="Calculate",
    command=run_calculation,
    width=20
)
calc_button.pack(pady=(10, 5))

result_label = tk.Label(
    action_frame,
    text="",
    font=("Courier New", 15, "bold"),
    bg="#1A1A24",
    fg="#00FF00"
)
result_label.pack(pady=20)

update_inputs(None)

window.mainloop()