a = input("").split(" ")

s = int(a[0])
t = int(a[1])
f = int(a[2])

hora_final = (s+t) + f

if(hora_final == 24):
    hora_final = 0
elif (hora_final > 24):
    hora_final = hora_final % 24
elif (hora_final < 0):
    hora_final = 24 + hora_final
    
print(hora_final)