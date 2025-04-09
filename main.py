import customtkinter as ctk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image, ImageTk
import os

ctk.set_appearance_mode("system")  # Automaticamente claro ou escuro, conforme o Windows
ctk.set_default_color_theme("green")  # ou você pode customizar

def selecionar_imagem():
    caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.jpeg")])
    if not caminho:
        return
    try:
        imagem = Image.open(caminho)
        imagem.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(imagem)
        imagem_preview.configure(image=img_tk)
        imagem_preview.image = img_tk
        caminho_imagem.set(caminho)
        status_label.configure(text="Imagem carregada com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def remover_fundo():
    caminho = caminho_imagem.get()
    if not caminho:
        messagebox.showwarning("Atenção", "Selecione uma imagem primeiro.")
        return
    try:
        status_label.configure(text="Removendo fundo...")
        with open(caminho, 'rb') as input_file:
            input_data = input_file.read()
            output_data = remove(input_data)

        nome_arquivo = os.path.basename(caminho)
        novo_nome = f"sem_fundo_{nome_arquivo.split('.')[0]}.png"
        caminho_saida = os.path.join(os.path.dirname(caminho), novo_nome)

        with open(caminho_saida, 'wb') as output_file:
            output_file.write(output_data)

        status_label.configure(text="Fundo removido com sucesso!")
        messagebox.showinfo("Finalizado", f"Imagem salva em:\n{caminho_saida}")
    except Exception as e:
        status_label.configure(text="Erro.")
        messagebox.showerror("Erro", str(e))

# App
app = ctk.CTk()
app.geometry("450x600")
app.title("Removedor de Fundo")
app.configure(fg_color="#f3f4f6")

# Variáveis
caminho_imagem = ctk.StringVar()

# Título
ctk.CTkLabel(app, text="Removedor de Fundo", font=("Segoe UI", 22, "bold"), text_color="#1f2937").pack(pady=(20, 10))

# Botão Selecionar Imagem
ctk.CTkButton(app, text="Selecionar Imagem", command=selecionar_imagem, fg_color="#a78bfa", hover_color="#c4b5fd", corner_radius=20).pack(pady=10)

# Preview
imagem_preview = ctk.CTkLabel(app, text="", width=300, height=300, bg_color="#e5e7eb")
imagem_preview.pack(pady=20)

# Botão Remover Fundo
ctk.CTkButton(app, text="Remover Fundo", command=remover_fundo, fg_color="#a78bfa", hover_color="#c4b5fd", corner_radius=20).pack(pady=10)

# Status
status_label = ctk.CTkLabel(app, text="Aguardando imagem...", text_color="#4b5563", font=("Segoe UI", 12, "italic"))
status_label.pack(pady=15)

# Start
app.mainloop()
