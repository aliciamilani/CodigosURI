resp = input().split(" ")

n1 = int(resp[0])
n2 = int(resp[1])
n3 = int(resp[2])
maior = 0
if (n1>n2 and n1>n3):
    maior = n1
    if ((maior- (n2+n3))== 0 ):
        print("S") 
    else:
        print("N")
        
if (n2>n1 and n2>n3):
    maior = n2
    if ((maior- (n1+n3))== 0 ):
        print("S")
    else:
        print("N")
if (n3>n1 and n3>n2):
    maior = n3
    if ((maior- (n2+n1))== 0 ):
        print("S")
    else:
        print("N")

if( n1 ==n2 or n1 == n3 or n2 == n3 ):
    print('S')

