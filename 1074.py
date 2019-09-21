qtde = int(input())

for i in range(qtde):
    num = int(input())
    if(num == 0 ):
        mens = "NULL"
    else:
        if(num%2==0):
            mens = "EVEN"
        else:
            mens = "ODD"
        if(num>=0):
            mens += " POSITIVE"
        else:
            mens += " NEGATIVE"
    print(mens)
