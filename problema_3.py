import random as rnd


def normal(m, v):
    suma = 0.0
    for _ in range(12):
        r = rnd.random()
        suma += r
    prome = suma/12
    tmp = (prome-0.5)/(1/12)
    resp = tmp*v+m
    return resp


def uniforme(a, b):
    r = rnd.random()
    return r*(b-a)+a


def simula(tini, tfin, m, v, a, b):
    t = tini
    nFila = 0
    # Llegada del primer cliente
    tllega = t+normal(m, v)
    # Fila vacia, por lo tanto el tiempo de servicio del siguiente cliente es muy grande
    tsalida = 1000
    # Cuantos clientes atiende el servidor
    nClientes = 0

    while t <= tfin:
        if tllega <= tsalida:
            t = tllega
            if nFila == 0:
                # Salida del cliente si no habia nadie en la fila
                tsalida = t+uniforme(a, b)
            nFila += 1
        else:
            t = tsalida
            nFila -= 1
            if nFila > 0:
                # Salida del siguiente en la fila
                tsalida = t+uniforme(a, b)
            if nFila == 0:
                # La fila esta vacia
                tsalida = 1000
            nClientes += 1
        # Llegada del siguiente cliente a la fila
        tllega = t+normal(3, 1)
    return nClientes


def simula_2(tini, tfin, nClientes, m, v, a, b):
    t = tini
    tllega = t + normal(m, v)
    tsale = 1000
    nFila = 0
    nAtendido = 0

    while t <= tfin:
        if tllega <= tfin:
            t = tllega
            if nFila == 0:
                tsale = t + uniforme(a, b)
            nFila += 1
        else:
            t = tsale
            nClientes -= 1
            nAtendido += 1
            if nClientes > 0:
                tsale = t + uniforme(a, b)
            if nClientes == 0:
                tsale = 1000
        tllega = t + normal(m, v)
    return nAtendido


def ppal():
    nAtendidos = simula(0, 120, 4, 1, 4, 4)
    nAtendidos2 = simula_2(0, 120, nAtendidos, 1, 1, 5, 5)
    print("El segundo servidor recibio " + str(nAtendidos) +
          " clientes del servidor 1 y atendio " + str(nAtendidos2) + " clientes")


if __name__ == "__main__":
    ppal()
