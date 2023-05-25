import random as rnd
import threading as thr

## Funciones normal y uniforme aqui
def normal(m, v):
    suma = 0
    for _ in range(12):
        r = rnd.random()
        suma += r
    prome = suma / 12
    tmp = (prome - 0.5) / (1 / 12)
    resp = tmp + v + m
    return resp

def uniforme(a, b):
    r = rnd.random()
    return r * (b - a) + a



## Funcion simula aqui
def simula(tini,tfin, nClientes,m,v,a,b):
	t=tini
	tllega=t+normal(m,v)
	tsale=1000
	nFila=0
	nAtendidos=0
	maxClientes=9999
	while t <= tfin:
		if tllega <= tsale:
			t=tllega
			if nFila==0:
				tsale=t+uniforme(a,b)
			nFila+=1
		else:
			t=tsale
			maxClientes-=1
			nAtendidos+=1
			if maxClientes > 0:
				tsale=t+uniforme(a,b)
			if maxClientes==0:
				tsale=1000
		tllega=t+normal(m,v)
	nClientes.append(nAtendidos)
	return


def ppal():
	nClientes1=[]
	nClientes2=[]
	fila1=thr.Thread(target=simula,args=(0,120,nClientes1,5,1,6,6))
	fila2=thr.Thread(target=simula,args=(0,120,nClientes2,4,1,6,6))
	fila1.start()
	fila2.start()
	fila1.join()
	fila2.join()
	print("El  server1 atendio" + str(nClientes1) + "clientes")
	print("El  server2 atendio" + str(nClientes2) + "clientes")
if __name__ == "__main__":
	ppal()

