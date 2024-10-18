import os
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_heigth = root.winfo_screenheight()

title_label = tk.Label(
    root,
    text='VendaFácil v0.1.0',
    font=("Arial", 16)
)

title_label.pack()

main_frame = tk.Frame(
    root,
    width=screen_width,
    height=screen_heigth,
)

main_frame.pack(fill="both", expand=True)

image = Image.open(os.getcwd() + '/assets/bg.jpg')
image = image.resize((screen_width, screen_heigth), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(image)

vendas_icon = ImageTk.PhotoImage(Image.open(os.getcwd() + '/assets/icons/sell.png').resize((50, 50)))
estoque_icon = ImageTk.PhotoImage(Image.open(os.getcwd() + '/assets/icons/storage.png').resize((50, 50)))
dashboard_icon = ImageTk.PhotoImage(Image.open(os.getcwd() + '/assets/icons/dashboard.png').resize((50, 50)))
fornecedores_icon = ImageTk.PhotoImage(Image.open(os.getcwd() + '/assets/icons/box.png').resize((50, 50)))
forma_pagamento_icon = ImageTk.PhotoImage(Image.open(os.getcwd() + '/assets/icons/payment-way.png').resize((50, 50)))
sair_icon = ImageTk.PhotoImage(Image.open(os.getcwd() + '/assets/icons/exit.png').resize((50, 50)))



bg_canvas = tk.Canvas(main_frame, width=screen_width, height=screen_heigth)
bg_canvas.pack(fill="both", expand=True)

bg_canvas.create_image(0, 0, image=bg_image, anchor="nw")

root.geometry(f"{screen_width}x{screen_heigth}+0+0")

root.title('VendaFácil - Menu principal')

btn_container_frame = tk.Frame(
    bg_canvas,
    width=600,
    height=600,
    border=30
)


btn_container_frame.grid(pady=screen_heigth*0.30, padx=screen_width*0.35, sticky="nsew")

btn_vendas = tk.Button(btn_container_frame, text="Vendas", image=vendas_icon, compound=tk.TOP)
btn_estoque = tk.Button(btn_container_frame, text="Estoque", image=estoque_icon, compound=tk.TOP)
btn_dashboard = tk.Button(btn_container_frame, text = "Dashboard", image=dashboard_icon, compound=tk.TOP)
btn_meios_pagamento = tk.Button(btn_container_frame, text = "Meios de Pagamento", image=forma_pagamento_icon, compound=tk.TOP)
btn_fornecedores = tk.Button(btn_container_frame, text = "Fornecedores", image=forma_pagamento_icon, compound=tk.TOP)
btn_sair = tk.Button(btn_container_frame, text="Sair", image=sair_icon, compound=tk.TOP)


btn_vendas.grid(row=1, column=1, padx=10)
btn_estoque.grid(row=1, column=2, padx=10)
btn_dashboard.grid(row=1, column=3, padx=10)
btn_fornecedores.grid(row=2, column=1, padx=10, pady=10)
btn_meios_pagamento.grid(row=2, column=2, padx=10, pady=10)
btn_sair.grid(row=2, column=3, padx=10, pady=10)

root.mainloop()