resp = input().split(" ")
cod = int(resp[0])
qtde = int(resp[1])
preco = 0
if(cod == 1):
    preco = 4.00
elif (cod == 2):
    preco = 4.50
elif (cod == 3):
    preco = 5.00
elif (cod == 4):
    preco = 2.00
elif (cod == 5):
    preco = 1.50
tot = preco * qtde
print("Total: R$ %.2f"%tot)