tupla = (13, 1, 8, 3, 2, 5, 8)
tupla_lista = []
for i in tupla:
    if i >= 5:
        continue
    tupla_lista.append(i)
print(tupla_lista)