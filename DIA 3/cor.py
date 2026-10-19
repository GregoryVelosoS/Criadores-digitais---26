from colorama import Fore, Back, Style
import time

print(Style.BRIGHT)

#Fore
print("Hoje é só:")
time.sleep(0.5)
print(Fore.RED + "Texto top e vermelho")
print("OI")
time.sleep(2)
print(Fore.YELLOW + "Texto top, só que agora, amarelo")
print("Tchau")
time.sleep(2)
print(Fore.GREEN + "Acabou, agora em verde, pra acabar o semáforo")
print("Fica com Deus")
time.sleep(2)
print(Fore.CYAN + "Falei que ia acabar, mas menti")
print("E de vez em quando um boa noite")

#Back
print(Back.MAGENTA + "Sei lá que cor essa")
print(Back.LIGHTBLACK_EX + "Deve ser preto, só mais claro")
print(Back.LIGHTWHITE_EX + "top ai esse fundo")

#Reset 
print(Style.RESET_ALL)