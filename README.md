# Removedor de fundo

Aplicativo em Python com uma interface moderna para remover o fundo de imagens.  
Feito por Gabriel.

## 🚀 Tecnologias Utilizadas

-  Python 
-  CustomTkinter (interface moderna)
-  rembg (remoção de fundo)
-  Pillow (manipulação de imagens)
-  PyInstaller (geração de executável)

## 💻 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/gabrielosiqueira/removedor-fundo.git
cd removedor-fundo
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
.\venv\Scripts\activate  
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

python main.py

## Como gerar o .exe

```bash
pyinstaller --noconsole --onefile --icon=icone.ico main.py
```

O executável aparecerá em dist/main.exe



