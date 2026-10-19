#Importa outra biblioteca
#random = aleatório
import random

#randint - número aleatório e inteiro
print("Número sorteado:", random.randint(0,10))

#uniform - número aleatório decimal
print("Número sorteado:", random.uniform(0,1))

#Adivinhação - Faça o computador sortear um número, solicite ao usuário um número inteiro, e compare para descobrir se é igual ao que o computador sorteou

# Número sorteado
sorteado = random.randint(0,1)

# for - laço de repetição
# contador - conta quantas vezes eu já repeti
# range(x,y,z)
# x = inicio da contagem, y = fim da contagem
# z - o valor do incremento  
for contador in range(0,3,1):
    print("Oi")
    print(contador)

# Usuário tenta acertar o número 3x
for contador in range(0,3,1):
    print("---------------------------------------")
    print("TENTE ADIVINHAR O NÚMERO QUE EU SORTEEI")
    # Pedir o número para o usuário
    numero = int(input("Qual o seu palpite:"))

    #Compara os números
    if(sorteado == numero):
        print("Parabéns, você acertou!!!")
        break
    else:
        print("Puxa, infelizmente, você não é o brabo")

