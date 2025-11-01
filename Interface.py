# Importando dependências do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk # widgets estilizados
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import ImageTk, Image  # Manipulação de imagens logo e fotos
from tkcalendar import Calendar, DateEntry
from datetime import date


# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"  # letra
co6 = "#146C94"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + verde

# criando janela
janela = Tk()
janela.title("Sistema de Registro de Colaboradores")
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)
janela.attributes('-alpha', 0.9)

# Criando frames
Frame_logo = Frame(janela, width=900, height=50, bg=co6)
Frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

Frame_corpo = Frame(janela, width=900, height=550, bg=co9, relief="flat")
Frame_corpo.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

Frame_botoes = Frame(Frame_corpo, width=880, height=50, bg=co9, relief="raised")
Frame_botoes.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

Frame_detalhes = Frame(Frame_corpo, width=880, height=500, bg=co1, relief="solid")
Frame_detalhes.grid(row=1, column=0, pady=1, padx=10, sticky=NSEW)

Frame_tabela = Frame(Frame_corpo, width=880, height=500, bg=co9, relief="solid")
Frame_tabela.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

# Inserindo logo
global image, imagem_string, I_imagem

try:
    app_logo = Image.open('logo.png')
    app_logo = app_logo.resize((50, 50))
    app_logo = ImageTk.PhotoImage(app_logo)
except:
    app_logo = None

app_logo_logo = Label(Frame_logo, image=app_logo, text="Sistema de Registro de Colaboradores", 
                     width=850, compound=LEFT, anchor=NW, font=("Verdana", 15), bg=co6, fg=co1)
app_logo_logo.place(x=10, y=0)

# Criando área para foto do colaborador
I_imagem = Label(Frame_detalhes, bg=co1, fg=co4)
I_imagem.place(x=700, y=10)


# Criando campos de entrada
# Campo Nome
l_nome = Label(Frame_detalhes, text="Nome:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(Frame_detalhes, width=45, justify='left', relief='solid')
e_nome.place(x=10, y=40)

# Campo E-mail
l_email = Label(Frame_detalhes, text="E-mail:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_email.place(x=10, y=70)
e_email = Entry(Frame_detalhes, width=45, justify='left', relief='solid')
e_email.place(x=10, y=100)

# Campo Telefone
l_telefone = Label(Frame_detalhes, text="Telefone:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_telefone.place(x=10, y=130)
e_telefone = Entry(Frame_detalhes, width=45, justify='left', relief='solid')
e_telefone.place(x=10, y=160)

# Campo Sexo
l_sexo = Label(Frame_detalhes, text="Sexo:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_sexo.place(x=10, y=190)
c_sexo = ttk.Combobox(Frame_detalhes, width=20, justify='left')
c_sexo['values'] = ('Masculino', 'Feminino', 'Outro')
c_sexo.place(x=10, y=220)

# Campo Data de Nascimento
l_data_nascimento = Label(Frame_detalhes, text="Data de Nascimento:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_data_nascimento.place(x=10, y=250)
e_data_nascimento = DateEntry(Frame_detalhes, width=20, background='darkblue', foreground='white', borderwidth=2, year=date.today().year)
e_data_nascimento.place(x=10, y=280)

# Campo Endereço
l_endereco = Label(Frame_detalhes, text="Endereço:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_endereco.place(x=10, y=310)
e_endereco = Entry(Frame_detalhes, width=45, justify='left', relief='solid')
e_endereco.place(x=10, y=340)

# Campo Loja
l_loja = Label(Frame_detalhes, text="Loja:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_loja.place(x=350, y=10)
e_loja = Entry(Frame_detalhes, width=45, justify='left', relief='solid')
e_loja.place(x=350, y=40)

# Campo Endereço da Loja
l_endereco_loja = Label(Frame_detalhes, text="Endereço da Loja:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_endereco_loja.place(x=350, y=70)
e_endereco_loja = Entry(Frame_detalhes, width=45, justify='left', relief='solid')
e_endereco_loja.place(x=350, y=100)

# Campo Data de Admissão
l_data = Label(Frame_detalhes, text="Data de Admissão:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_data.place(x=350, y=130)
e_data = DateEntry(Frame_detalhes, width=20, background='darkblue', foreground='white', borderwidth=2, year=date.today().year)
e_data.place(x=350, y=160)

# Campo Fim do Contrato
l_fim_contrato = Label(Frame_detalhes, text="Fim do Contrato:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_fim_contrato.place(x=350, y=190)
e_fim_contrato = DateEntry(Frame_detalhes, width=20, background='darkblue', foreground='white', borderwidth=2, year=date.today().year)
e_fim_contrato.place(x=350, y=220)

# Campo Cargo
l_cargo = Label(Frame_detalhes, text="Cargo:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cargo.place(x=350, y=250)
e_cargo = Entry(Frame_detalhes, width=45, justify='left', relief='solid')
e_cargo.place(x=350, y=280)

# Campo Salário
l_salario = Label(Frame_detalhes, text="Salário:", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_salario.place(x=350, y=310)
e_salario = Entry(Frame_detalhes, width=45, justify='left', relief='solid')
e_salario.place(x=350, y=340)

# Função para escolher foto
def escolher_foto():
    global image, imagem_string, I_imagem

    # Abrir a janela para escolher a foto
    caminho_foto = fd.askopenfilename(title="Escolher Foto", filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])
    if caminho_foto:
        # Carregar a imagem escolhida
        image = Image.open(caminho_foto)
        image = image.resize((130, 130))
        imagem_string = ImageTk.PhotoImage(image)
        I_imagem.configure(image=imagem_string)

# Botão para escolher foto
botao_escolher_foto = Button(Frame_detalhes, command=escolher_foto, text="ESCOLHER FOTO", width=20,
                           compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8 bold'),
                           bg=co1, fg=co0)
botao_escolher_foto.place(x=700, y=160)

# Tabela de Funcionários
tabela_funcionarios = ttk.Treeview(Frame_tabela, columns=("ID", "Nome", "e-mail", "Telefone", "Sexo", "Data_Nascimento", "Endereco", "loja", "Endereco_Loja", "data_admissao", "fim_contrato", "Cargo", "Salário"), show="headings")
tabela_funcionarios.heading("ID", text="ID")
tabela_funcionarios.heading("Nome", text="Nome")
tabela_funcionarios.heading("e-mail", text="E-mail")
tabela_funcionarios.heading("Telefone", text="Telefone")
tabela_funcionarios.heading("Sexo", text="Sexo")
tabela_funcionarios.heading("Data_Nascimento", text="Data de Nascimento")
tabela_funcionarios.heading("Endereco", text="Endereço")
tabela_funcionarios.heading("loja", text="Loja")
tabela_funcionarios.heading("Endereco_Loja", text="Endereço da Loja")
tabela_funcionarios.heading("data_admissao", text="Data de Admissão")
tabela_funcionarios.heading("fim_contrato", text="Fim do Contrato")
tabela_funcionarios.heading("Cargo", text="Cargo")
tabela_funcionarios.heading("Salário", text="Salário")
tabela_funcionarios.place(x=10, y=10)

# Botões de Ação
botao_salvar = Button(Frame_botoes, text="Salvar", width=10, font=('Ivy 8 bold'),
                     bg=co3, fg=co1, relief=RAISED, overrelief=RIDGE)
botao_salvar.place(x=10, y=10)

botao_atualizar = Button(Frame_botoes, text="Atualizar", width=10, font=('Ivy 8 bold'),
                        bg=co6, fg=co1, relief=RAISED, overrelief=RIDGE)
botao_atualizar.place(x=110, y=10)

botao_deletar = Button(Frame_botoes, text="Deletar", width=10, font=('Ivy 8 bold'),
                      bg=co7, fg=co1, relief=RAISED, overrelief=RIDGE)
botao_deletar.place(x=210, y=10)

#chamar tabela

tabela_funcionarios.place(x=10, y=10)

janela.mainloop()