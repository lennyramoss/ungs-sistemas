palabra = "neuquen"
ant=""
flag=False
vocales=["a","e","i","o","u"]
for char in palabra:
    if char in vocales:
        if ant in vocales:#no es == , se usa in recorre cada elemento
            flag=True
    ant=char

if flag:
    print("hay diptongo")