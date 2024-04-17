import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Dibujo")
        
        self.canvas = tk.Canvas(root, bg="white", width=400, height=400)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.setup_toolbar()
        
        self.setup_bindings()
        
        self.start_x = None
        self.start_y = None
        self.color = "black"
        self.brush_size = 2
        
    def setup_toolbar(self):
        self.toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        
        self.clear_button = tk.Button(self.toolbar, text="Limpiar lienzo", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)
        
        self.color_label = tk.Label(self.toolbar, text="Color:")
        self.color_label.pack(side=tk.LEFT)
        
        self.color_button = tk.Button(self.toolbar, text="Seleccionar", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT)
        
        self.brush_label = tk.Label(self.toolbar, text="Tamaño del pincel:")
        self.brush_label.pack(side=tk.LEFT)
        
        self.brush_slider = tk.Scale(self.toolbar, from_=1, to=10, orient=tk.HORIZONTAL, command=self.change_brush_size)
        self.brush_slider.set(2)
        self.brush_slider.pack(side=tk.LEFT)
        
        self.eraser_button = tk.Button(self.toolbar, text="Borrador", command=self.use_eraser)
        self.eraser_button.pack(side=tk.LEFT)
        
    def setup_bindings(self):
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)
        
    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y
        
    def draw(self, event):
        if self.start_x and self.start_y:
            x, y = event.x, event.y
            self.canvas.create_line(self.start_x, self.start_y, x, y, fill=self.color, width=self.brush_size)
            self.start_x, self.start_y = x, y
            
    def end_draw(self, event):
        self.start_x = None
        self.start_y = None
        
    def clear_canvas(self):
        self.canvas.delete("all")
        
    def choose_color(self):
        self.color = tk.colorchooser.askcolor()[1]
        
    def change_brush_size(self, size):
        self.brush_size = int(size)
        
    def use_eraser(self):
        self.color = "white"

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
