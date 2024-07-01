# Requirements
import polars as pl
pl.Config(fmt_str_lengths=50)
pl.Config(tbl_rows=30)
import sys
import json
from unidecode import unidecode
import difflib

sys.path.insert(0, r'C:\Users\fscielzo\Documents\Packages\BigEDA_Package_Private')
from BigEDA.preprocessing import dtypes_df, change_type, prop_cols_nulls
from BigEDA.descriptive import summary, outliers_table, freq_table, cross_quant_cat_summary, contingency_table_2D
from BigEDA.plots import histogram_matrix, boxplot_matrix, ecdfplot_matrix, barplot_matrix, boxplot_2D_matrix

def find_most_similar_string(target, candidates):
    # Get a list of matches with their similarity ratio
    matches = difflib.get_close_matches(target, candidates, n=1, cutoff=0.0)
    # Return the most similar string
    return matches[0] if matches else None

# Reading the data
years = list(range(2019, 2025))
madrid_traffic_acc_df = {}
for year in years:
    madrid_traffic_acc_df[year] = pl.read_csv(fr'C:\Users\fscielzo\Documents\DataScience-GitHub\EDA\Madrid-Traffic-Accidents\data\{year}_Accidentalidad.csv', separator=';', ignore_errors=True)

# Removing columns
madrid_traffic_acc_df[2022] = madrid_traffic_acc_df[2022].select(pl.all().exclude(['', '_duplicated_0']))

# Replacing values
replace_dict = {}
replace_dict['estado_meteorológico'] = {'NULL': None, 'Se desconoce': None}
replace_dict['rango_edad'] = {'Desconocido': None}
replace_dict['sexo'] = {'Desconocido': None}
replace_dict['cod_lesividad'] = {'NULL': None}
replace_dict['lesividad'] = {'NULL': None, 'Se desconoce': None}
replace_dict['positiva_alcohol'] = {'NULL': None, 'N': False, 'S': True}
replace_dict['positiva_droga'] = {'NULL': False, '1': True}
replace_dict['coordenada_x_utm'] = {'NULL': None, "#¡VALOR!": None}
replace_dict['coordenada_y_utm'] = {'NULL': None, "#¡VALOR!": None}
replace_dict['tipo_persona'] = {'NULL': None}
replace_dict['tipo_vehiculo'] = {'NULL': None, 'Sin especificar': None}
replace_dict['distrito'] = {'NULL': None}
replace_dict['tipo_accidente'] = {'NULL': None}

for year in years:
    for col in replace_dict.keys():
        try:
            madrid_traffic_acc_df[year] = madrid_traffic_acc_df[year].with_columns(pl.col(col).replace(replace_dict[col]).alias(col))
        except:
            pass

# Changing data types
columns_to_change = ['coordenada_x_utm', 'coordenada_y_utm']
for year in years:
    for col in columns_to_change:
        try:
            madrid_traffic_acc_df[year] = madrid_traffic_acc_df[year].with_columns(madrid_traffic_acc_df[year][col].map_elements(lambda x: x.replace(',', '.')).cast(pl.Float64).alias(col))
        except:
            pass

# Concatenating the data
madrid_traffic_acc_df = pl.concat([madrid_traffic_acc_df[year] for year in years], how='vertical')

# Replacing more values
replace_dict = {}
replace_dict['rango_edad'] = {}
unique_values = madrid_traffic_acc_df['rango_edad'].unique().drop_nulls().to_list()
for i in range(len(unique_values)):
    limits = [x for x in unique_values[i].split(' ') if x.isdigit()]
    if len(limits) == 2:
        replace_dict['rango_edad'][unique_values[i]] = f'[{limits[0]},{limits[1]}]'
    elif len(limits) == 1:
        if 'Más' in unique_values[i].split(' '):
            replace_dict['rango_edad'][unique_values[i]] = f'> {limits[0]}'
        elif 'Menor' in unique_values[i].split(' '):
            replace_dict['rango_edad'][unique_values[i]] = f'< {int(limits[0])+1}'

unique_values = madrid_traffic_acc_df['tipo_vehiculo'].unique().drop_nulls().to_list()
replace_dict['tipo_vehiculo'] =  {x: 'Autobus' for x in unique_values if 'bus' in x or 'bús' in x}
replace_dict['tipo_vehiculo'].update({x: 'Moto' for x in unique_values if 'ciclo' in x.lower() or 'moto' in x.lower()})
replace_dict['tipo_vehiculo'].update({x: 'Maquinaria' for x in unique_values if 'maquinaria' in x.lower()})
replace_dict['tipo_vehiculo'].update({x: 'Patinete' for x in unique_values if 'patinete' in x.lower()})
replace_dict['tipo_vehiculo'].update({x: 'Remolque' for x in unique_values if 'remolque' in x.lower()})
replace_dict['tipo_vehiculo'].update({x: 'Otros' for x in unique_values if 'otros' in x.lower()})
replace_dict['tipo_vehiculo'].update({x: 'Bicicleta' for x in unique_values if 'bici' in x.lower()})

replace_dict['lesividad'] = {'Asistencia sanitaria inmediata en centro de salud o mutua': 'Asist. inmediata CS',
                             'Asistencia sanitaria ambulatoria con posterioridad': 'Asist. posterior CS',
                             'Ingreso inferior o igual a 24 horas': 'Ingreso <= 24h',
                             'Fallecido 24 horas': 'Fallecido',
                             'Atención en urgencias sin posterior ingreso': 'Urg. sin ingreso',
                             'Asistencia sanitaria sólo en el lugar del accidente': 'Asist. insitu',
                             'Ingreso superior a 24 horas': 'Ingreso > 24h',
                             'Sin asistencia sanitaria': 'Sin asist. sanitaria'
                             }

replace_dict['tipo_accidente'] = {'Solo salida de la vía': 'Salida via',
                                  'Atropello a animal': 'Atropello animal',
                                  'Atropello a persona': 'Atropello persona',
                                  'Choque contra obstáculo fijo': 'Choque obstaculo fijo'
                                  }

geojson_file = r'C:\Users\fscielzo\Documents\DataScience-GitHub\EDA\Madrid-Traffic-Accidents\data\madrid-districts.geojson'
with open(geojson_file) as f:
    madrid_geojson = json.load(f)
distritos_geojson = [madrid_geojson['features'][i]['properties']['name'] for i in range(len(madrid_geojson['features']))]
distritos_data = madrid_traffic_acc_df['distrito'].drop_nulls().unique().to_list()
replace_dict['distrito'] = {x: find_most_similar_string(unidecode(x.lower().title()), candidates=distritos_geojson) for x in distritos_data}

for col in replace_dict.keys():
    madrid_traffic_acc_df = madrid_traffic_acc_df.with_columns(pl.col(col).replace(replace_dict[col]).alias(col))


# Saving the resulting data-frame
madrid_traffic_acc_df.write_csv(r'C:\Users\fscielzo\Documents\DataScience-GitHub\EDA\Madrid-Traffic-Accidents\data\madrid_traffic_accidents.csv')