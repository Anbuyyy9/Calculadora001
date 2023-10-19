numero1 = input("Digite um numero") 
numero2 = input("Digite um segundo numero")

print("Digite uma operação 1_+  2_-  3_*   4_/  ")



contador = False

operacao = input("Digite a operação (1) (2) (3) (4)")


while contador == False:
    if numero1 >= 1000:
      print("Digite um numero valido: ")
    elif numero2 >= 1000:
       print("Digite um numero valido!!")
    else:
       continue

