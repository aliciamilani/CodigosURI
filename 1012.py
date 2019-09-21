#Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. 
# Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B. 

lista = input().split(" ")
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

print("TRIANGULO:", (A*C)/2)
print("CIRCULO:",3.14159 * (C**2))
print("TRAPEZIO:", ((A+B)*C)/2)
print("QUADRADO:", B**2)
print("RETANGULO:", A*B)