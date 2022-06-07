def mais_alto(la, lb):
    jog_mais_alto = lb.index(max(lb))
    return f'JOGADOR MAIS ALTO DO TIME\n{la[jog_mais_alto]}\n{max(lb):.2f}'

def media_time(lb):
    media = sum(lb) / len(lb)
    return f'ALTURA MÉDIA DO TIME\n{media:.2f}'

def media_altura(la, lb):
    media = sum(lb) / len(lb)
    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    for elemento in lb:
        if elemento > media:
            print(f'{la[lb.index(elemento)]}\n{elemento:.2f}')

def main():
    lista_nomes = []
    lista_alturas = []
    for termo in range(12):
        nome = input().strip()
        lista_nomes.append(nome)
        altura = float(input().strip())
        lista_alturas.append(altura)

    print(mais_alto(lista_nomes, lista_alturas))
    print(media_time(lista_alturas))
    media_altura(lista_nomes, lista_alturas)

if __name__ == '__main__':
    main()