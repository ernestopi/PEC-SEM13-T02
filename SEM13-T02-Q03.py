def lista_a():
    la = []
    for item in range(20):
        elemento = int(input().strip())
        la.append(elemento)
    return la

def lista_b():
    lb = []
    for item in range(20):
        elemento = int(input().strip())
        lb.append(elemento)
    return lb

def nova_lista(la, lb):
    lc = []
    for a, b in zip(la, lb):
        lc.append(a + b)
    return lc

def main():
    a = lista_a()
    b = lista_b()
    print(a)
    print(b)
    print(nova_lista(a, b))

if __name__ == '__main__':
    main()