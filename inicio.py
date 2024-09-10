import customtkinter as ctk
from PIL import Image      
import tkinter as tk
from tkinter import messagebox

ctk.set_appearance_mode("light")
janela = ctk.CTk()
janela.configure(bg='#FFFFFF')
janela.title("Calculadora :D")
janela.geometry("320x500")
janela.resizable(False, False)

# Início --------------------

janela1 = ctk.CTkFrame(janela, fg_color = "#ffd101")
janela1.pack(fill="both", expand = True)

# Fotos ---------------------

badtzmaru = ctk.CTkImage(
light_image=Image.open("badtzmaru.png"),
dark_image=Image.open("badtzmaru.png"),
size=(130, 60)
)

def imagem_tela (imagem, bgcolor, posicaox, posicaoy):

    image_label = ctk.CTkLabel(janela1, image=imagem, text="", bg_color = bgcolor)
    image_label.place(relx=posicaox, rely=posicaoy, anchor="center")

imagem_tela(badtzmaru, "transparent", 0.12, 0.08)

# Funções Desing -------------

def quadrados(cor, bgcolor, width, height,posicaox, posicaoy):
    ctk.CTkFrame(
    master = janela1, 
    width= width, 
    height= height,
    fg_color = cor,
    bg_color = bgcolor

    ).place(relx=posicaox, rely=posicaoy, anchor="center")

quadrados("#ffffff", "transparent", 230, 33, 0.58, 0.08)
quadrados("#292929", "White", 87, 20, 0.77, 0.08 )
# quadrados("#ffffff", "transparent", 230, 50, 0.58, 0.19)
quadrados("#fcdc49", "transparent", 500, 500, 0.5, 0.8)
quadrados("black", "transparent", 5, 290, 0.9, 0.62)

def textos(texto, fonte, tamanho, cor_texto, fundo_texto, posicaox, posicaoy):
    bemvindo = ctk.CTkLabel(
        janela1, 
        text= texto,
        font=(fonte, tamanho, "bold"),
        text_color= cor_texto,
        fg_color= fundo_texto
        )
    bemvindo.place(relx= posicaox, rely= posicaoy, anchor="center")

textos("Calculadora", "Arial", 20, "#1a1a1a", "White", 0.42, 0.08)

# Funções Botões -------------

def inserir(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + key)

def calcular():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

def limpar():
    entry.delete(0, tk.END)

def inverter_sinal():
    current = entry.get()
    if current:
        try:
            num = float(current)
            num = -num
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(num))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Erro")

entry = ctk.CTkEntry(janela1, width=230, height=50, font=("Arial", 24), border_color= "white")
entry.place(relx=0.58, rely=0.2, anchor="center")

buttons = [
    ('7', 0.14, 0.5), ('8', 0.33, 0.5), ('9', 0.52, 0.5),
    ('4', 0.14, 0.62), ('5', 0.33, 0.62), ('6', 0.52, 0.62),
    ('1', 0.14, 0.74), ('2', 0.33, 0.74), ('3', 0.52, 0.74),
    ('±', 0.14, 0.86),('0', 0.33, 0.86), ('.', 0.52, 0.86),
    ('+', 0.71, 0.5), ('-', 0.71, 0.62),
    ('*', 0.71, 0.74), ('/', 0.71, 0.86),
    ('C', 0.14, 0.38), ('=', 0.43, 0.38), (':D', 0.71, 0.38)
]

for (text, row, column) in buttons:
    if text == 'C':
        button = ctk.CTkButton(
            janela1, 
            text=text, 
            width = 50, 
            height = 50, 
            fg_color="#292929", 
            hover_color = "#3b3a3a",
            font=("Arial", 15),
            command=limpar)
        
    elif text == '=':
        button = ctk.CTkButton(
            janela1, 
            text=text,
            width = 113, 
            height = 50, 
            fg_color="#f7a025",
            hover_color = "#ed961a",
            font=("Arial", 15),
            command=calcular)
        
    elif text == '±':
        button = ctk.CTkButton(
            janela1,
            text=text, 
            width=50, 
            height=50, 
            fg_color="#292929",
            hover_color="#3b3a3a", 
            font=("Arial", 15), 
            command=inverter_sinal)
        
    elif text == ':D':
        button = ctk.CTkButton(
            janela1,
            text= text, 
            width=50, 
            height=50, 
            fg_color="#292929",
            hover_color="#3b3a3a", 
            font=("Arial", 15), 
            command=lambda t="Tenha um ótimo dia": inserir(t)
            )
        
    else:
        button = ctk.CTkButton(
            janela1,
            text=text, 
            width = 50, 
            height = 50, 
            fg_color="#292929",
            hover_color = "#3b3a3a", 
            font=("Arial", 15), 
            command=lambda t=text: inserir(t))
        
    button.place(relx=row, rely=column, anchor="center")

janela.mainloop()