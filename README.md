# spanish-aemet-data-map-generator

Code that generates a map of couplings of the values obtained by the meteorological stations in the different Spanish provinces of AEMET (http://www.aemet.es/es/portada) 

The variables supported by this code are:

| id | description
| :---: | --- |
| prec | Precipitación acumulada, medida por el pluviómetro, durante los 60 minutos anteriores a la hora indicada por el período de observación 'fint' (mm, equivalente a l/m2) |
| pacutp | Precipitación acumulada, medida por el disdrómetro, durante los 60 minutos anteriores a la hora indicada por el período de observación 'fint' (mm, equivalente a l/m2) |
| pliqtp | Precipitación líquida acumulada durante los 60 minutos anteriores a la hora indicada por el período de observación 'fint' (mm, equivalente a l/m2) |
| psolt | Precipitación sólida acumulada durante los 60 minutos anteriores a la hora indicada por el período de observación 'fint' (mm, equivalente a l/m2) |
| vmax | Velocidad máxima del viento, valor máximo del viento mantenido 3 segundos y registrado en los 60 minutos anteriores a la hora indicada por el período de observación 'fint' (m/s) |
| vv | Velocidad media del viento, media escalar de las muestras adquiridas cada 0,25 ó 1 segundo en el período de 10 minutos anterior al indicado por 'fint' (m/s) |
| vmaxu | Velocidad máxima del viento (sensor ultrasónico), valor máximo del viento mantenido 3 segundos y registrado en los 60 minutos anteriores a la hora indicada por el período de observación 'fint' (m/s) |
| vvu | Velocidad media del viento (sensor ultrasónico), media escalar en el periódo de 10 minutos anterior al indicado por 'fint' de las muestras adquiridas cada 0,25 ó 1 segundo (m/s) |
| dv | Dirección media del viento, en el período de 10 minutos anteriores a la fecha indicada por 'fint' (grados) |
| dvu | Dirección media del viento (sensor ultrasónico), en el período de 10 minutos anteriores a la fecha indicada por 'fint' (grados) |
| dmax | Dirección del viento máximo registrado en los 60 minutos anteriores a la hora indicada por 'fint' (grados) |
| dmaxu | Dirección del viento máximo registrado en los 60 minutos anteriores a la hora indicada por 'fint' por el sensor ultrasónico (grados) |
| stdvv | Desviación estándar de las muestras adquiridas de velocidad del viento durante los 10 minutos anteriores a la fecha dada por 'fint' (m/s) |
| stddv | Desviación estándar de las muestras adquiridas de la dirección del viento durante los 10 minutos anteriores a la fecha dada por 'fint' (grados) |
| stdvvu | Desviación estándar de las muestras adquiridas de velocidad del viento durante los 10 minutos anteriores a la fecha dada por 'fint' obtenido del sensor ultrasónico de viento instalado junto al convencional (m/s) |
| stddvu | Desviación estándar de las muestras adquiridas de la dirección del viento durante los 10 minutos anteriores a la fecha dada por 'fint' obtenido del sensor ultrasónico de viento instalado junto al convencional (grados) |
| hr | Humedad relativa instantánea del aire correspondiente a la fecha dada por 'fint' (%) |
| inso | Duración de la insolación durante los 60 minutos anteriores a la hora indicada por el período de observación 'fint' (horas) |
| pres | Presión instantánea al nivel en el que se encuentra instalado el barómetro y correspondiente a la fecha dada por 'fint' (hPa) |
| pres_nmar | Valor de la presión reducido al nivel del mar para aquellas estaciones cuya altitud es igual o menor a 750 metros y correspondiente a la fecha indicada por 'fint' (hPa) |
| ts | Temperatura suelo, temperatura instantánea junto al suelo y correspondiente a los 10 minutos anteriores a la fecha dada por 'fint' (grados Celsius) |
| tss20cm | Temperatura subsuelo 20 cm, temperatura del subsuelo a una profundidad de 20 cm y correspondiente a los 10 minutos anteriores a la fecha dada por 'fint' (grados Celsius) |
| tss5cm | Temperatura subsuelo 5 cm, temperatura del subsuelo a una profundidad de 5 cm y correspondiente a los 10 minutos anteriores a la fecha dada por 'fint' (grados Celsius) |
| ta | Temperatura instantánea del aire correspondiente a la fecha dada por 'fint' (grados Celsius) |
| tpr | Temperatura del punto de rocío calculado correspondiente a la fecha 'fint' (grados Celsius) |
| tamin | Temperatura mínima del aire, valor mínimo de los 60 valores instantáneos de 'ta' medidos en el período de 60 minutos anteriores a la hora indicada por el período de observación 'fint' (grados Celsius) |
| tamax | Temperatura máxima del aire, valor máximo de los 60 valores instantáneos de 'ta' medidos en el período de 60 minutos anteriores a la hora indicada por el período de observación 'fint' (grados Celsius) |
| vis | Visibilidad, promedio de la medida de la visibilidad correspondiente a los 10 minutos anteriores a la fecha dada por 'fint' (Km) |
| geo700 | Altura del nivel de la superficie de referencia barométrica de 700 hPa calculado para las estaciones con altitud mayor de 2300 metros y correspondiente a la fecha indicada por 'fint' (m geopotenciales) |
| geo850 | Altura del nivel de la superficie de referencia barométrica de 850 hPa calculado para las estaciones con altitud mayor de 1000 metros y menor o igual a 2300 metros y correspondiente a la fecha indicada por 'fint' (m geopotenciales) |
| geo925 | Altura del nivel de la superficie barométrica de 925 hPa calculado para las estaciones con altitud mayor de 750 metros y y menor o igual a 1000 metros correspondiente a la fecha indicada por 'fint' (m geopotenciales) |
| rviento | Recorrido del viento durante los 60 minutos anteriores a la fecha indicada por 'fint' (Hm) |
| nieve | Espesor de la capa de nieve medid en los 10 minutos anteriores a la a la fecha indicada por 'fint' (cm) |

Example  1           |  Example2
:-------------------------:|:-------------------------:
![](https://github.com/Guillermo-C-A/spanish-aemet-data-map-generator/blob/master/Some%20examples/ta_temporal_map2019-08-19T16:00:00.png)  |  ![](https://github.com/Guillermo-C-A/spanish-aemet-data-map-generator/blob/master/Some%20examples/ta_temporal_map2019-08-20T13:00:00.png)

Provinces example 1 | Temps. example 1 | Provinces example 2 | Temps. example 2
:---:|:---:|:---:|:---:|
ARABA/ALAVA | 19.1 | ARABA/ALAVA | 20.2 
ALBACETE | 34.35 | ALBACETE | 30.525 |
ALICANTE | 29.53333333333333 | ALICANTE | 31.1 |
ALMERIA | 29.44 | ALMERIA | 28.920000000000005 |
AVILA | 24.933333333333334 | AVILA | 25.96666666666667 |
... | ... | ... | ... |
BIZKAIA | 18.825 | BIZKAIA | 20.85 |
ZAMORA | 25.5 | ZAMORA | 24.03333333333333 |
ZARAGOZA | 24.12 | ZARAGOZA | 21.94 |
MELILLA | 33.4 | MELILLA | 31.6 |
CEUTA | 32.9 | CEUTA | 29.9 |
