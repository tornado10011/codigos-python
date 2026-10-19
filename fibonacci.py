print("fibonacci")

a=0
b=1

fibo=int(input("digite el numero del fibonacci que desea sacar: "))

for i in range(1, fibo+1):   
    final=a+b
    a=b
    b=final
    

print(final)