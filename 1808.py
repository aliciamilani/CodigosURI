a = str(input())
soma = 0
cont_zero = 0
for i in a:
    soma+=int(i)
    if int(i) == 0:
        cont_zero+=1
        soma+=9
media = soma / (len(a) - cont_zero)

print('{:.2f}'.format(media))