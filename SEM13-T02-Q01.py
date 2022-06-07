def comprimento(l):
    q = 0
    for i in l:
        q += 1
    return f'{l}\n{q}'

def inverter(l):
    inverso = []
    for i in l:
        inverso.insert(0, i)
    return inverso

def minimo(l):
    menor = 999999999999999999
    for i in l:
        if i < menor:
            menor = i
    return menor

def maximo(l):
    maior = 0
    for i in l:
        if i > maior:
            maior = i
    return maior

def soma(l):
    adicao = 0
    for i in l:
        adicao += i
    return adicao

def main():
    lista = []
    while True:
        valor = int(input().strip())
        if valor == 0:
            break
        else:
            lista.append(valor)
    print(comprimento(lista))
    print(inverter(lista))
    print(minimo(lista))
    print(maximo(lista))
    print(soma(lista))

if __name__ == '__main__':
    main()