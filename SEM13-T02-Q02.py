def frequencia(l, termo):
    contador = 0
    for i in l:
        if i == termo:
            contador += 1
    return f'{l}\n{termo}\n{contador}'

def main():
    lista = []
    while True:
        valor = int(input().strip())
        if valor == 0:
            break
        else:
            lista.append(valor)
    numero = int(input().strip())
    print(frequencia(lista, numero))

if __name__ == '__main__':
    main()