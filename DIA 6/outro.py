# Importação biblioteca
import customtkinter as ctki

# Cores e fonte 
cor_principal = "#FFFFFF"
cor_secundaria = "#FF0000"
cor_texto = "#000000"
cor_sucesso = "#00A100"
cor_erro = "#FF0000"
fonte_padrao = ("Segoe UI", 20, "bold")

#Criação e definição da tela
janela = ctki.CTk()

# Alterando o nome da tela
janela.title("Login Tela")

#Aumentar o tamanho da tela
janela.geometry("500x350")

#Define a cor de fundo
janela.configure( fg_color = cor_principal )

# CRIAR ELEMENTOS NA MINHA PÁGINA
# CtkLabel = Cria textos na tela
titulo = ctki.CTkLabel(
    janela, text = "Faça seu login ✋😜✋",
    font= ("Arial", 40, "bold"), text_color = "#F039B1"
)

#Anexa o texto na tela
#pady = cria espaços entre os elementos no eixo y
titulo.pack(pady = "10")

# Texto usuário
txt_usuario = ctki.CTkLabel(
    janela, text= "Usuário", font= fonte_padrao, text_color= cor_texto
)
txt_usuario.pack(pady="10")

# Input usuário
cx_usuario = ctki.CTkEntry(
    janela, placeholder_text="Digite seu usuário", justify='center'
)
cx_usuario.pack(pady='10')

# Texto senha
txt_senha = ctki.CTkLabel(
    janela, text= "senha", font= fonte_padrao, text_color= cor_texto
)
txt_senha.pack(pady="10")

# Input senha
cx_senha = ctki.CTkEntry(
    janela, placeholder_text="Digite seu senha", justify='center'
)
cx_senha.pack(pady='10')

# Botão de login
def verificar_login():
    #Pega os valores das caixinhas e põe em variáveis
    usuario = cx_usuario.get()
    senha = cx_senha.get()

    #Verificar o login
    if(usuario == "Cristiano" and senha == "1234"):
        txt_final.configure( text= "LOGIN REALIZADO", text_color = cor_sucesso)
    else:
        txt_final.configure( text= "USUÁRIO INVÁLIDO", text_color = cor_erro)

# Botão de login
botao_login = ctki.CTkButton( janela, text= "Fazer login", fg_color= cor_secundaria,
    command = verificar_login, hover_color= cor_texto)
botao_login.pack(pady="16")

#Texto resposta
txt_final = ctki.CTkLabel( janela, text= "", font= fonte_padrao)
txt_final.pack(pady="10")

#CÓDIGO QUE SEMPRE FICA NO FIM
janela.mainloop()