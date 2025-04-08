import tkinter as tk
from tkinter import Canvas
from objects import Plane


class VisualizePlane:
    def __init__(self, plane: Plane, canvas: Canvas) -> None:
        self.plane = plane
        self.canvas = canvas

        self.step = min(self.plane.width // 10, self.plane.height // 10)
        self.margin = max(self.plane.width // 10, self.plane.height // 10)

        self.canvasWidth = self.margin * 2 + self.plane.width
        self.canvasHeight = self.margin * 4 + self.plane.height


    def Run(self) -> None:
        originX = self.margin
        originY = self.margin + self.plane.height

        self.canvas.create_line(originX, originY, originX + self.plane.width + 10, originY, fill='white', arrow=tk.LAST)
        self.canvas.create_line(originX, originY, originX, originY - self.plane.height - 10, fill='white', arrow=tk.LAST)

        for x in range(0, self.plane.width + 1, self.step):
            screenX = originX + x

            if 0 <= screenX <= self.canvasWidth:
                self.canvas.create_line(screenX, originY, screenX, originY - self.plane.height, fill='gray', dash=(3, 5))
                self.canvas.create_text(screenX, originY + 20, text=str(x), fill='white', font=('Arial', 10))

        for y in range(0, self.plane.height + 1, self.step):
            screenY = originY - y

            if 0 <= screenY <= self.canvasHeight:
                self.canvas.create_line(originX, screenY, originX + self.plane.width, screenY, fill='gray', dash=(3, 5))
                self.canvas.create_text(originX - 20, screenY, text=str(y), fill='white', font=('Arial', 10))
