# FAÇA UM ALGORITMO QUE PEÇA: NOME, NOTA1 E NOTA2

print("Oi, bem vindo")

# Pegar as inforamações
nome = input("Me diga seu nome:")
nota1 = float( input("Informe a nota 1:") )
nota2 = float( input("Informe a nota 2:") )

# Faz o cálculo da média
media = (nota1 + nota2) / 2

# Condicional
# 6+ = passou
if(media >= 6):
    print("Você foi aprovado")
# entre 6 e 5 = recuperação
if(media < 6 and media >= 5):
    print("Você está de recuperação")
# menos que 5 = reprovou
if(media < 5):
    print("Infelizmente, você reprovou")

print("Fim de código!!!")