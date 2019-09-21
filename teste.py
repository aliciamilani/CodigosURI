i = 0
while i < 5:
    x = input("")
    print(x)
    if x is None:
        print("aa")
    if(x != '/n' and x != "" and x!= None):
        print("entrou")
        i += 1
    else: 
        continue