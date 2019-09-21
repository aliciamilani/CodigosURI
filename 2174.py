qtde = int(input(""))
pok = []
for i in range(qtde):
    nome = input("")
    pok.append(nome)

atual = len(sorted(set(pok)))
faltam = 151 - atual

print("Falta(m) %d pomekon(s)."%faltam)