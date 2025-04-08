import tkinter as tk
from tkinter import Canvas
from objects import Plane
from plane import VisualizePlane
from text import VisualizeText


class App:
    def __init__(self, plane: Plane, title: str) -> None:
        self.root = tk.Tk()
        self.root.title(title)

        self.plane = plane
        self.margin = max(plane.width // 10, plane.height // 10)

        self.canvasWidth = self.margin * 2 + plane.width
        self.canvasHeight = self.margin * 4 + plane.height

        self.canvas = Canvas(self.root, width=self.canvasWidth, height=self.canvasHeight, bg='black')
        self.canvas.pack()


    def Run(self) -> None:
        VisualizePlane(self.plane, self.canvas).Run()
        VisualizeText(self.root, self.plane, self.canvas).Run()
        self.root.mainloop()


if __name__ == '__main__':
    plane = Plane(width=500, height=500, locus=set())
    app = App(plane, "Geometry Calculator", )
    app.Run()
