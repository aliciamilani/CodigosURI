instancias = int(input(""))

for i in range(instancias):
    bonus = int(input(""))
    n1 = input("").split(" ")
    ataque_d = int(n1[0])
    defesa_d = int(n1[1])
    level_d = int(n1[2])

    n2 = input("").split(" ")
    ataque_g = int(n2[0])
    defesa_g = int(n2[1])
    level_g = int(n2[2])
    
    #O Bônus será dado ao Pomekon do treinador que estiver em um level de valor par.
    
    golpe_d = (ataque_d + defesa_d)/2 
    if (level_d % 2 == 0):
        golpe_d += bonus 

    golpe_g = (ataque_g + defesa_g)/2 
    if (level_g % 2 == 0):
        golpe_g += bonus 
    
    if(golpe_d == golpe_g):
        print("Empate")
    elif (golpe_d>golpe_g):
        print("Dabriel")
    elif (golpe_g>golpe_d):
        print("Guarte")