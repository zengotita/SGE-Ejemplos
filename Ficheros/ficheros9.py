lista = ['1', '2', '3']

with open("fichero123.txt", "w+") as f:
    f.write(str(lista))

print(f.name)

with open("fichero123.txt", "r") as f:
    e=f.read()

print(e)