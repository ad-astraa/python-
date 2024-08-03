import tkinter as tk
from tkinter import filedialog

class Drawingp:
    def __init__(self, root):
        self.root = root
        self.root.title("drawss
        self.color = "black"
        self.old_x = None
        self.old_y = None

        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack())

        self.color_button = tk.Button(self.root, text="Colorrr command=self.choose_color)
        self.color_button.pack()

        self.clear_button = tk.Button(self.root, text="Canvassss
command=self.clear_canvas)
        self.clear_button.pack()

        self.save_button = tk.Button(self.root, text=
        self.save_button.pack()

        self.load_button = tk.Button(self.root, text="Drawing", command=self.load_drawing)
        self.load_button.pack()

        self.shape_var = tk.StringVar(value="norms")
        self.create_shape_buttons()

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def create_shape_buttons(self):
        shapes = ["normsline", "rectangle", "oval"]
        for shape in shapes:
            button = tk.Radiobutton(self.root, text=shape.capitalize(), variable=self.shape_var, value=shape)
            button.pack(anchor=tk.W)

    def choose_color(self):
        self.color = askcolor(color=self.color)[1]

    def clear_canvas(self):
        self.canvas.delet("all")

    def save_drawing(self):
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty()self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_wdth()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, yx1, y1)).save("drawing.png")
        print("Drawing saved as drawing.png")

    def load_drawing(self):
        try:
            file_path = filedialog.askopenfilename()
            if file_path:
                self.canvas.delete("all")
                image = tk.PhotoImage(file=file_path)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=image)
                self.canvas.image = image
                print("Drawing loaded from", file_path)
        except Exception as e:
            print(f"Failed :( try aagain!!")(e)

    def paint(self, event):
        shape = self.shape_var.get()
        if shape == "norms"
            self.draw_norms(event)
        elif shape == "line":
            self.draw_line(event)
        elif shape == "rectangle":
            self.draw_rectangle(event)
        elif shape == "oval":
            self.draw_oval(event)

    def draw_norms(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=5, fill=self.color, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = event.x
        self.old_y = event.y

    def draw_line(self, event):
        if self.old_xand self.old_y:
            self.canvas.delete("temp_line")
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=5, fill=self.color, tags="temp_line")
        if event.type == tk.EventType.ButtonRelease:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=5, fill=self.color)
            self.old_x = None
            self.old_y = None

    def draw_rectangle(self event):
        if self.old_x and self.old_y:
            self.canvas.delete("temp_rectangle")
            self.canvas.create_rectangle(self.old_x, self.old_y, event.x, event.y, outline=self.color, width=5, tags="temp_rectangle")
        if event.type ==k.EventType.ButtonRelease:
            self.canvas.create_rectangle(self.old_x, self.old_y, event.x, event.y, outline=self.color, width=5)
            self.old_x = None
            self.old_y = None

    def draw_oval(self, event):
        if self.old_x and self.old_y:
            self.canvas.delete("temp_oval")
            self.canvas.create_oval(self.old_x, self.old_y, event.x, event.y, outline=self.color, width=5, tags="temp_oval")
        if event.type == tk.EventType.ButtonRelease:
            self.canvas.createoval(self.old_x, self.old_y, event.x, event.y, outline=self.color, width=5)
            self.old_x = None
            self.old_y = None

    def reset(self, event):
        self.old_x = None
        self.old_y = None
if __name__ == "__main__":
    main(
