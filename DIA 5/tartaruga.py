#IMPORTAR O MÓDULO DA TARTARUGA
import turtle

#Criando a tela de pintura
tela = turtle.Screen()
#Definir tamanho da tela. width=largura, height=600
tela.setup(width=800, height=600)
# Trocar o nome na tela
tela.title("Desenhando com a turtle")

#Criando a turtle
mbappe = turtle.Turtle()
#Mudando o formato
mbappe.shape("turtle")

#forward - anda pra frente
# mbappe.forward(200)
#backward - anda para trás
# mbappe.backward(500)
#right - vira a direita
# mbappe.right(90)
#left - vira a esquerda
# mbappe.left(180)

#Quadrado
for x in range(4):
    mbappe.forward(200)
    mbappe.left(90)

# Quadrado ao quadrado
for y in range(4):
    for x in range(4):
        mbappe.forward(200)
        mbappe.left(90)
    mbappe.left(90)

#Limpar a tela de pintura
mbappe.clear()

#TROCAR A COR
#da caneta
mbappe.pencolor("white")
#do fundo
tela.bgcolor("red")
# tamanho da linha
mbappe.pensize(1)

# #fazer um circulo
# mbappe.circle(50)

#altera a velocidade
mbappe.speed('fastest')
contador_cor = 0

# Top circulo top
for x in range(1):
    mbappe.circle(x)
    mbappe.left(1)
    if(contador_cor == 0):
        mbappe.pencolor("white")
    elif(contador_cor == 1):
        mbappe.pencolor("black")
    elif(contador_cor == 2):
        mbappe.pencolor("blue")
    elif(contador_cor == 3):
        mbappe.pencolor("green")
    elif(contador_cor == 4):
        mbappe.pencolor("yellow")
    else:
        contador_cor = 0 
    contador_cor = contador_cor + 1

#Limpar a tela de pintura
mbappe.clear()

#Voltar ao centro
mbappe.home()

# Ativa a escuta de comando
tela.listen()

#def - defini funcoes
def moverFrente():
    mbappe.forward(100)

def girarDireita():
    mbappe.right(90)

def girarEsquerda():
    mbappe.left(90)

# Executar funções quando apertar uma tecla
tela.onkey(girarDireita, "Right")
tela.onkey(girarEsquerda, "Left")
tela.onkey(moverFrente, "Up")

# DEIXA ISSO AQUI NO FINAL SEMPRE
# Só sai quando clica
tela.exitonclick()