lista = [6,2,5,5,4,5,6,3,7,6]
x = int(input())

for i in range(x):
    a = input()
    soma = 0
    for i in a:
        for j in range(len(lista)):
            if int(i) == j:
                soma +=int(lista[j])
    print(str(soma)+" leds")