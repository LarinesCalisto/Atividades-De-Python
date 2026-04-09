#calculadora de raiz quadrada
import math
#Solicita um númeroário
num= float(input("Digite um número para saber sua raiz quadrada: "))
if (num > 0):
    resultado= math.sqrt(num)
    print("O valor da raiz quadrada de", num, "é: ",resultado)
else:
    print("O númeo precisa ser maior q 0!!!! seu inteligente")
