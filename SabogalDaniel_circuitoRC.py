import numpy as np
import matplotlib.pyplot as plt
datos = np.genfromtxt("CircuitoRC.txt", usecols = (0,1))

Rguess = 11.0
Cguess = 7.0
Vo = 10.0
def carga(t,C,R):
	return (Vo*C)*(1-np.exp(-t/(float(R)*C)))
t = datos[:,0]
y = datos[:,1]
Yguess = carga(t,Cguess,Rguess)


n=1000

def L(Yprueba,Ydata):
	chicuadrado = 0.0
	for i in range(t.size):
		chicua = (Yprueba[i] - Ydata[i])**2
		chicuadrado = chicuadrado + chicua
	return np.exp(chicuadrado*(-1.0/20000.0))

		
	
	
Lguess = L(Yguess,y)

Cpaso =  []
Rpaso = []
Lpaso = []

Cpaso.append(Cguess)
Rpaso.append(Rguess)
Lpaso.append(Lguess)
dC = 0.5
dR = 10.0
for i in range(n):
	if(i==0):
		Yantigua = Yguess
		Rantigua = Rguess
		Cantigua = Cguess
		Lantigua = Lguess
	Cnueva = np.random.normal(Cpaso[i],dC)
	Rnueva = np.random.normal(Rpaso[i],dR)
	Ynueva = carga(t,Cnueva,Rnueva)
	Lnueva = L(Ynueva,y)
	print Lnueva
	
	
	alfa = Lnueva/float(Lantigua)
	if (alfa>1):
		Lpaso.append(Lnueva)
		Rpaso.append(Rnueva)
		Cpaso.append(Cnueva)

	else:
		beta = np.random.rand(1)
		if(beta>alfa):
			Lpaso.append(Lnueva)
			Rpaso.append(Rnueva)
			Cpaso.append(Cnueva)
		else:
			
			Lpaso.append(Lantigua)
			Rpaso.append(Rantigua)
			Cpaso.append(Cantigua)
	Rantigua = Rnueva
	Cantigua = Cnueva
	Yantigua = Ynueva
	Lantigua = Lnueva

Lmax = max(Lpaso)
for i in range(n):
	if(Lpaso[i]==Lmax):
		imax = i


Ccorrecto = Cpaso[imax]
Rcorrecto =Rpaso[imax]

ycorrecto = carga(t,Ccorrecto,Rcorrecto)
plt.figure()
plt.plot(t,ycorrecto)
plt.scatter(t,ycorrecto)
plt.savefig("CargaRC.pdf")



	

	
