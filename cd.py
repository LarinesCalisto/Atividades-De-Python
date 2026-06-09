for i in range (10,1,-1): 

numeros = [1,2,3,4,5]
for num in reversed(numeros):
    print (num)

contador = 10 
while contador >= 0:
        print (contador)
contador -=1


#inversão de 3 numeros (tipo4)
num= int(input("Digite um número com 3 digitos: "))

#Digitos
d1= num// 100       #centena
d2=(num%100)//10    #dezena
d3= num % 10        #unidade

#Invertendo o número
inverso= d3 * 100 + d2 * 10 + d1

#Resultado
print("O inverso do número digitado é : ", inverso)

