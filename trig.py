import tkinter as tk
from tkinter import messagebox
import math

def calc_trig():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("+ve only bro.")

        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("invalid aaa:( .")

        angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_C = 180 - angle_A - angle_B

        sin_A = math.sin(math.radians(angle_A))
        cos_A = math.cos(math.radians(angle_A))
        tan_A = math.tan(math.radians(angle_A))

        sin_B = math.sin(math.radians(angle_B))
        cos_B = math.cos(math.radians(angle_B))
        tan_B = math.tan(math.radians(angle_B))

        trig_values.set(f"Angle A: {angle_A:.2f}°\n"
                        f"Angle B: {angle_B:.2f}°\n"
                        f"Angle C: {angle_C:.2f}°\n\n"
                        f"sin(A) = {sin_A:.2f}\n"
                        f"cos(A) = {cos_A:.2f}\n"
                        f"tan(A) = {tan_A:.2f}\n\n"
                        f"sin(B) = {sin_B:.2f}\n"
                        f"cos(B) = {cos_B:.2f}\n"
                        f"tan(B) = {tan_B:.2f}")

        draw_triangle(a, b, c)

    except ValueError as e:
        messagebox.showerror("errrorr", str(e))

def draw_triangle(a, b, c)::
    canvas.delete("all")
    scale = 200 / max(a, b, c)
    a_scaled = a * scale
    b_scaled = b * scale
    c_scaled = c * scale

    canvas.create_line(50, 300, 50 + b_scaled, 300, width=2)
    canvas.create_line(50, 300, 50, 300 - a_scaled, width=2)
    canvas.create_line(50, 300 - a_scaled, 50 + b_scaled, 300, width=2)

    canvas.create_text(25, 300 - a_scaled / 2, text=f"a = {a:.2f}", fill="red")
    canvas.create_text(50 + b_scaled / 2, 315, text=f"b = {b:.2f}", fill="blue")
    canvas.create_text(50 + b_scaled / 2, 300 - a_scaled / 2, text=f"c = {c:.2f}", fill="green")

root = tk.Tk()
root.title("Trig Calc")
root.configure(bg='#FFB6C1')

tk.Label(root, text="Side a:", bg='#FFB6C1').grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Side b:", bg='#FFB6C1').grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

tk.Label(root, text="Side c (hypotenuse):", bg='#FFB6C1').grid(row=2, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calc_trig, bg='#FF1493', fg='white').grid(row=3, columnspan=2)

trig_values = tk.StringVar()
tk.Label(root, textvariable=trig_values, justify=tk.LEFT, bg='#FFB6C1').grid(row=0, column=2, rowspan=4, padx=10)

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.grid(row=0, column=3, rowspan=4)

root.mainloop()
