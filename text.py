import tkinter as tk
import bindings as bds
from tkinter import Canvas
from objects import Plane


class VisualizeText:
    def __init__(self, root: tk.Tk, plane: Plane, canvas: Canvas) -> None:
        self.root = root
        self.plane = plane
        self.canvas = canvas

        self.margin = max(self.plane.width // 10, self.plane.height // 10)

        self.textBox = tk.Text(
            self.root,  undo=True,
            bd=False,   highlightthickness=False,
            fg='white', insertbackground='white',
            bg='black', font=('Arial', 10)
        )

        self.prefix = ">> "
        self.postfix = "1.0"

        self.textBox.bind("<Key>", self.OnKey)
        self.textBox.bind("<Return>", self.OnReturn)
        self.textBox.bind("<BackSpace>", self.OnBack)


    def OnKey(self, event: tk.Event) -> str:
        return bds.OnKey(self.textBox, self.postfix)

    def OnBack(self, event: tk.Event) -> str:
        return bds.OnBack(self.textBox, self.postfix)

    def OnReturn(self, event: tk.Event) -> str:
        self.postfix = bds.OnReturn(self.textBox, self.prefix, "\n")
        return "break"


    def Run(self) -> None:
        self.postfix = bds.OnReturn(self.textBox, self.prefix)

        originX1 = self.margin
        originX2 = self.margin + self.plane.width
        originY1 = self.margin * 2 + self.plane.height
        originY2 = self.margin * 3 + self.plane.height

        self.canvas.create_rectangle(
            originX1, originY1, originX2, originY2,
            fill='black', outline='white', dash=(3, 5)
        )

        self.textBox.place(
            x=originX1 + 5,              y=originY1 + 5,
            width=self.plane.width - 10, height=self.margin - 10
        )
