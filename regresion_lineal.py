
valores_x = [0, 20, 30, 40, 50, 60]
valores_y = [100, 140, 200, 180, 250, 230]

def media(array):
    suma = 0

    for i in array:
        suma += i
    
    return suma / len(array)

def desviacion(array, media):
    diferencia = 0
    suma = 0
    for i in array:
        diferencia = ( i - media) ** 2
        suma += diferencia
    return ( suma / (len(array)-1) ) ** 0.5


media_x = media(valores_x)
media_y = media(valores_y)

# desviacion de xy
mult_medias = media_y * media_x
suma = 0
for i in range(0, len(valores_x)):
    diferencia = valores_x[i] * valores_y[i] - mult_medias
    suma += diferencia
covarianzaxy = suma / (len(valores_x) - 1)

# desviacion de x
desviacion_x = desviacion(valores_x, media_x)

# desviacion de y
desviacion_y = desviacion(valores_y, media_y)

correlacion = covarianzaxy / ( desviacion_y * desviacion_x)

pendiente = correlacion * ( desviacion_y / desviacion_x)
constante = media_y - pendiente * media_x

# funcion de regresion lineal

def f(x):
    return pendiente * x + constante

esperado_y = []

for i in range(0, len(valores_y)):
    esperado_y.append(f(valores_x[i]))

sumatoria = 0
for i in range(0, len(esperado_y)):
    diferencia = (esperado_y[i] - valores_y[i]) ** 2
    sumatoria += diferencia

ecm = sumatoria / len(valores_y)

print('La ecuación de regresión lineal es: ' + str(round(pendiente, 2)) + 'x + ' + str(round(constante, 2)))
print('El error cuadrático medio es: ' + str(ecm))
