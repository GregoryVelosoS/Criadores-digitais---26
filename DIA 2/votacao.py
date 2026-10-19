print("Oi, bem vindo")

ano_nasc = int(input("Digite o ano de nascimento:"))

idade = 2026 - ano_nasc

#if() = primeira opção
#elif() = segunda opção caso a primeira dê errado
#else = ultimo caso, se todos antes derem errado

if(idade >=18):
    print("Você é OBRIGADO a votar")
elif(idade >=16):
    print("Pode votar !!!")
else:
    print("Não pode votar")