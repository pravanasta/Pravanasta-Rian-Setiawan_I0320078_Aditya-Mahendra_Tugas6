print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("====================       Mulai        ===================")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")

for x in range(10,25):
    for y in range(2,x):
        if (x % y) == 0:
            print(x,"bukan prima")
            break
    else:
        print(x,"adalah bilangan prima")
    
print("")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("===================       SELESAI        ==================")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")