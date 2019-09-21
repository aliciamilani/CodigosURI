info = input("").split()
trocas = int(info[0])
frases = int(info[1])

i = 0

lista1 = []
lista2 = []
list_frases = []
cont = True

while i < trocas:
    x = input("")
    if(x != '/n' and x != " " and x != "" and x != None):
        x = x.split()
        lista1.append(x[0])
        lista2.append(x[1])
        i += 1
    else: 
        continue


for i in range(frases):
    a = input("")
    list_frases.append(a)

for i in range(frases):
    for j in range(len(list_frases[i])):
        for k in range(len(lista1)):
            p=0
            if(p == 0):
                if (list_frases[i][j] == lista1[k]):
                    list_frases[i] = list_frases[i][j].replace(list_frases[i][j], lista2[k])
                    p = 1
            if(p == 0):
                if (list_frases[i][j] == lista2[k]):
                    list_frases[i] = list_frases[i][j].replace(list_frases[i][j], lista1[k])
                    p = 1

for i in range(frases):
    print(list_frases[i])
