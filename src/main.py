import os
import tkinter as tk
from PIL import Image, ImageTk
from views.components.IconButton import IconButton

def main():
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.title('VendaFácil - Menu principal')

    title_label = tk.Label(
        root,
        text='VendaFácil v0.1.0',
        font=("Arial", 16)
    )
    title_label.pack()

    main_frame = tk.Frame(
        root,
        width=screen_width,
        height=screen_height,
    )
    main_frame.pack(fill="both", expand=True)

    image = Image.open(os.path.join(os.getcwd(), 'assets/bg.jpg'))
    image = image.resize((screen_width, screen_height), Image.LANCZOS)  # Atualizando para LANCZOS
    bg_image = ImageTk.PhotoImage(image)

    bg_canvas = tk.Canvas(main_frame, width=screen_width, height=screen_height)
    bg_canvas.pack(fill="both", expand=True)
    bg_canvas.create_image(0, 0, image=bg_image, anchor="nw")

    btn_container_frame = tk.Frame(
        bg_canvas,
        border=15
    )
    btn_container_frame.pack(pady=screen_height*0.35, padx=screen_width*0.35, expand=True, fill=tk.BOTH) 

    btn_vendas = IconButton('Vendas', btn_container_frame, os.path.join('assets', 'icons', 'sell.png'))
    btn_dashboard = IconButton('Dashboard', btn_container_frame, os.path.join('assets', 'icons', 'dashboard.png'))
    btn_estoque = IconButton('Estoque', btn_container_frame, os.path.join('assets', 'icons', 'storage.png'))
    btn_fornecedores = IconButton('Fornecedores', btn_container_frame, os.path.join('assets', 'icons', 'box.png'))
    btn_meios_pagamento = IconButton('Meios de Pagamento', btn_container_frame, os.path.join('assets', 'icons', 'payment-way.png'))
    btn_saida = IconButton('Sair', btn_container_frame, os.path.join('assets', 'icons', 'exit.png'))

    btn_vendas.grid(row=1, column=1, padx=15)  
    btn_dashboard.grid(row=1, column=2, padx=15)
    btn_estoque.grid(row=1, column=3, padx=15)
    btn_fornecedores.grid(row=2, column=1, padx=15)
    btn_meios_pagamento.grid(row=2, column=2, padx=15)
    btn_saida.grid(row=2, column=3, padx=15)

    root.mainloop()

main()
