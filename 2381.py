a = input("").split(" ")

n = int(a[0])
k = int(a[1])
alunos = []

for i in range(n):
    nome = input("")
    alunos.append(nome)

alunos.sort()

print(alunos[k-1])