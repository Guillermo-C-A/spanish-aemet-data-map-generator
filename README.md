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

SOME EXAMPLES

![Alt text](https://github.com/Guillermo-C-A/spanish-aemet-data-map-generator/blob/master/Some%20examples/ta_temporal_map2019-08-19T16:00:00.png?style=centerme 'SAMPLE RESULT')

| Povince | Temperature ºC |
| :---: | :---: |
| ARABA/ALAVA | 19.1 |
| ALBACETE | 34.35 |
| ALICANTE | 29.53333333333333 |
| ALMERIA | 29.44 |
| AVILA | 24.933333333333334 |
| BADAJOZ | 32.48333333333333 |
| ILLES BALEARS | 29.29 |
| BARCELONA | 26.98 |
| BURGOS | 19.32 |
| CACERES | 31.2 |
| CADIZ | 26.85 |
| CASTELLON | 25.3 |
| CIUDAD REAL | 34.459999999999994 |
| CORDOBA | 34.525 |
| A CORUÑA | 19.275 |
| CUENCA | 32.65000000000001 |
| GIRONA | 24.5 |
| GRANADA | 34.300000000000004 |
| GUADALAJARA | 28.2 |
| GIPUZKOA | 19.075000000000006 |
| HUELVA | 28.125 |
| HUESCA | 23.85 |
| JAEN | 35.16 |
| LEON | 20.625 |
| LLEIDA | 25.2 |
| LA RIOJA | 22.9 |
| LUGO | 18.9 |
| MADRID | 27.211111111111112 |
| MALAGA | 32.642857142857146 |
| MURCIA | 31.9625 |
| NAVARRA | 19.925 |
| OURENSE | 23.700000000000006 |
| ASTURIAS | 18.04 |
| PALENCIA | 17.833333333333332 |
| LAS PALMAS | 26.575000000000006 |
| PONTEVEDRA | 22.8 |
| SALAMANCA | 22.660000000000004 |
| STA. CRUZ DE TENERIFE | 27.33333333333333 |
| CANTABRIA | 18.18 |
| SEGOVIA | 21.450000000000006 |
| SEVILLA | 34.1 |
| SORIA | 18.4 |
| TARRAGONA | 26.65 |
| TERUEL | 29.175 |
| TOLEDO | 32.92 |
| VALENCIA | 29.28333333333333 |
| VALLADOLID | 22.7 |
| BIZKAIA | 18.825 |
| ZAMORA | 25.5 |
| ZARAGOZA | 24.12 |
| MELILLA | 33.4 |
| CEUTA | 32.9 |

![Alt text](https://github.com/Guillermo-C-A/spanish-aemet-data-map-generator/blob/master/Some%20examples/ta_temporal_map2019-08-20T13:00:00.png?style=centerme 'SAMPLE RESULT 2')

| Povince | Temperature ºC |
| :---: | :---: |
| ARABA/ALAVA | 20.2 |
| ALBACETE | 30.525 |
| ALICANTE | 31.1 |
| ALMERIA | 28.920000000000005 |
| AVILA | 25.96666666666667 |
| BADAJOZ | 31.9 |
| ILLES BALEARS | 27.4 |
| BARCELONA | 26.08 |
| BURGOS | 20.380000000000006 |
| CACERES | 32.0 |
| CADIZ | 25.866666666666664 |
| CASTELLON | 19.475 |
| CIUDAD REAL | 32.7 |
| CORDOBA | 31.625 |
| A CORUÑA | 21.9875 |
| CUENCA | 28.7 |
| GIRONA | 18.133333333333336 |
| GRANADA | 31.3 |
| GUADALAJARA | 22.066666666666666 |
| GIPUZKOA | 21.075000000000006 |
| HUELVA | 29.05 |
| HUESCA | 21.75 |
| JAEN | 32.64 |
| LEON | 21.625 |
| LLEIDA | 18.45 |
| LA RIOJA | 23.4 |
| LUGO | 21.7 |
| MADRID | 25.766666666666666 |
| MALAGA | 28.214285714285715 |
| MURCIA | 31.25 |
| NAVARRA | 22.25 |
| OURENSE | 25.35 |
| ASTURIAS | 20.05 |
| PALENCIA | 19.966666666666672 |
| LAS PALMAS | 26.6625 |
| PONTEVEDRA | 26.25 |
| SALAMANCA | 24.22 |
| STA. CRUZ DE TENERIFE | 25.829999999999995 |
| CANTABRIA | 20.76 |
| SEGOVIA | 21.15 |
| SEVILLA | 32.32 |
| SORIA | 20.5 |
| TARRAGONA | 23.275 |
| TERUEL | 19.05 |
| TOLEDO | 30.62 |
| VALENCIA | 26.91666666666667 |
| VALLADOLID | 24.3 |
| BIZKAIA | 20.85 |
| ZAMORA | 24.03333333333333 |
| ZARAGOZA | 21.94 |
| MELILLA | 31.6 |
| CEUTA | 29.9 |


