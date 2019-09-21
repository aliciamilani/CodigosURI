ent = input().split()

n = int(ent[0])
k = int(ent[1])
resultados = []

a = input().split()

i=0
while i < n:
    j = i+1
    while(j < n):
        l = j+1
        while(l < n):
            b = 0
            b = int(a[i]) + int(a[j]) + int(a[l])
            b = b/3
            resultados.append(b)
            l+=1
        j+=1
    i+=1     

resultados.sort(reverse=True)
print("%.1f"%resultados[k-1])