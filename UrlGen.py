# File to create the Base Url
# https://www.adidas.ca/en/gazelle-shoes/BB5478.html?forceSelSize=BB5478_530 Size=4

def UrlGen(name,model,size):
     # Size for the shoe
     base=530
     mySize=(size-4)*20
     finalSize=base+mySize
     Url="https://www.adidas.ca/en/"+name+"/"+model+".html?forceSelSize="+model+"_"+str(finalSize)
     print(Url)

name = input("Name : ")
model = input("Model : ")
size = int(input("Size : "))
UrlGen(name,model,size)


