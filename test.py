import tkinter as tk

class AplicacionDibujo:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Dibujo Simple")

        # Configuración de la interfaz
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # Configuración de los botones
        self.clear_button = tk.Button(root, text="Limpiar", command=self.limpiar_dibujo)
        self.clear_button.pack(side=tk.BOTTOM)

        # Configuración del pincel
        self.color_pincel = "black"
        self.tamanio_pincel = 2

        # Configuración del dibujo
        self.dibujando = False
        self.canvas.bind("<B1-Motion>", self.dibujar)
        self.canvas.bind("<Button-1>", self.iniciar_dibujo)
        self.canvas.bind("<ButtonRelease-1>", self.detener_dibujo)

    def dibujar(self, evento):
        if self.dibujando:
            x1, y1 = (evento.x - self.tamanio_pincel), (evento.y - self.tamanio_pincel)
            x2, y2 = (evento.x + self.tamanio_pincel), (evento.y + self.tamanio_pincel)
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.color_pincel, outline=self.color_pincel, width=self.tamanio_pincel * 2)

    def iniciar_dibujo(self, evento):
        self.dibujando = True

    def detener_dibujo(self, evento):
        self.dibujando = False

    def limpiar_dibujo(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionDibujo(root)
    root.mainloop()
