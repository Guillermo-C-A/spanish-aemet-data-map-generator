import requests
from requests import get
from json import loads
import matplotlib.pyplot as plt
import geopandas
from pandas import DataFrame

class Aemet():
    
    def __init__(self):
        
        try:

            file = open('aemet_api.txt', 'r')
            self.key = file.readlines()[0].strip()
            file.close()
                
        except Exception as e:
            print(e)
    
    def aemet_api_call(self, url):
        
        querystring = {"api_key":self.key}

        headers = {
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.json()['datos']
 
        return DataFrame.from_dict(get(url=data).json())
    
    def merge_data(self):
        
        aemet_data = self.aemet_api_call('https://opendata.aemet.es/opendata/api/observacion/convencional/todas')
        aemet_stations = self.aemet_api_call('https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones')
        
        return aemet_data.merge(aemet_stations, left_on='idema', right_on='indicativo', how='inner')
    
    def plot_map(self, variable, title=''):
        
        final_data = self.merge_data()[['fint', 'provincia', variable]]
        final_data = final_data.groupby(['fint', 'provincia']).mean().reset_index()
        print(final_data)
        
        map_aemet = geopandas.read_file('provincias.shp')[['NOM_PROV', 'geometry']]
        
        for time in final_data['fint'].unique():
            
            aux_frame = final_data[final_data['fint'] == time]
            aux_frame = map_aemet.merge(aux_frame, left_on='NOM_PROV', right_on='provincia')
            
            aux_frame.plot(column=variable, legend=True, cmap='OrRd')
            plt.suptitle(title)
            plt.title(time)            
        
            plt.savefig(variable + '_' + 'temporal_map' + time + '.png')
            final_data[final_data['fint'] == time].to_csv(variable + '_' + 'temporal_map' + time +'.txt', sep=';')
y = Aemet()
y.plot_map('ta', 'TEMPERATURAS EN ESPAÑA')
