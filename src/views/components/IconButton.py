import os
import tkinter
from PIL import ImageTk, Image

class IconButton:
    def __init__(self, label: str, container: object, path: str, width: int =50, height: int=50) -> None:
        print('Pasta:' + os.path.join(os.getcwd(), path))
        self.icon = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), path)).resize((width, height)))
        self.btn = tkinter.Button(container, text=label, image=self.icon, compound=tkinter.TOP)
        pass

    def grid(self, row, column, padx) -> None:
        self.btn.grid(row=row, column=column, padx=padx)

    