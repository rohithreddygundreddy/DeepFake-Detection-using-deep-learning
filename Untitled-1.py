with open("uses.txt","r") as fil:
    file=fil.read()
print(file.split())
la="LUC, HUC, KAS,EDE"
a=la.split()
b=",".join(a)
print(b)