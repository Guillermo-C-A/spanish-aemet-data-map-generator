from http.client import HTTPSConnection
from requests import get
from json import loads
import matplotlib.pyplot as plt
import geopandas
from pandas import DataFrame, concat

class Aemet():
    
    def __init__(self):
        
        try:

            file = open('aemet_api.txt', 'r')
            self.key = file.readlines()[0].strip()
            file.close()
                
        except Exception as e:
            print(e)
    
    def aemet_api_call(self, url):
        
        conn = HTTPSConnection("opendata.aemet.es")
            
        headers = {
            'cache-control': "no-cache"
            }
            
        conn.request("GET",
                     url + "/?api_key=" + self.key,
                     headers=headers)
            
        res = conn.getresponse()
        data = res.read()
        data = loads(data.decode("utf-8"))['datos']
 
        return DataFrame.from_dict(get(url=data).json())
    
    def merge_data(self):
        
        aemet_data = self.aemet_api_call('/opendata/api/observacion/convencional/todas')
        aemet_stations = self.aemet_api_call('/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones')
        
        return aemet_data.merge(aemet_stations, left_on='idema', right_on='indicativo', how='inner')
    
    def plot_map(self, variable, title=''):
        
        change_name = ['ARABA/ALAVA', 'ALBACETE', 'ALICANTE', 'ALMERIA', 'AVILA', 'BADAJOZ', 'ILLES BALEARS',
                     'BARCELONA', 'BURGOS', 'CACERES', 'CADIZ', 'CASTELLON', 'CIUDAD REAL', 'CORDOBA', 'A CORUÑA',
                     'CUENCA', 'GIRONA', 'GRANADA', 'GUADALAJARA', 'GIPUZKOA', 'HUELVA', 'HUESCA', 'JAEN', 'LEON',
                     'LLEIDA', 'LA RIOJA', 'LUGO', 'MADRID', 'MALAGA', 'MURCIA', 'NAVARRA', 'OURENSE', 'ASTURIAS',
                     'PALENCIA', 'LAS PALMAS', 'PONTEVEDRA', 'SALAMANCA', 'STA. CRUZ DE TENERIFE', 'CANTABRIA',
                     'SEGOVIA', 'SEVILLA', 'SORIA', 'TARRAGONA', 'TERUEL', 'TOLEDO', 'VALENCIA', 'VALLADOLID',
                     'BIZKAIA', 'ZAMORA', 'ZARAGOZA', 'MELILLA', 'CEUTA']
        
        final_data = self.merge_data()
        data_time = final_data.groupby('fint')
        final_data = []
        
        map_aemet = geopandas.read_file('Provincias.shp')
        map_aemet['NOM_PROV'] = change_name
        
        for data_frame in data_time:
            
            date = data_frame[0]
            data = data_frame[1]
            
            aux_data = DataFrame()
            
            for province in data['provincia'].unique():
                aux = DataFrame([[province, data[data['provincia'] == province][variable].mean()]])
                aux_data = concat([aux_data, aux])
            
            aux_data.columns = ['provincia', variable]
            
            final_data = map_aemet.merge(aux_data, left_on='NOM_PROV', right_on='provincia')
            
            final_data.plot(column=variable, legend=True, cmap='OrRd')
            plt.suptitle(title)
            plt.title(date)
        
            plt.savefig(variable + '_' + 'temporal_map' + date + '.png')
            final_data[['provincia', variable]].to_csv(variable + '_' + 'temporal_map' + date +'.txt', sep=';')            

# EXAMPLE
y = Aemet()
y.plot_map('ta','Spanish temperature')
