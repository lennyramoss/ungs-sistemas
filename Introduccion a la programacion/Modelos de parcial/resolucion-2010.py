#1 
def palindromo(a):
    a = str(a)
    alreves=""
    for char in a:
        alreves= char + alreves
    if a==alreves:
        return True
    else:
        return False
    
print(palindromo(1578751))


