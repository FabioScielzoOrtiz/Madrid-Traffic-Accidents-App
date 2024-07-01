import streamlit as st
import polars as pl
import pandas as pd
import pandas as pd
import numpy as np
import pickle
from streamlit_extras.add_vertical_space import add_vertical_space 

# Utils
############################################################################

from utils import (multi_selector, display_descriptive_summary, display_frequency_tables, 
                   display_barplot, display_barplot_2D, display_barplot_2D_multiplot,
                   display_histogram, display_lineplot, display_scatterplot,
                   display_time_series_multiplot, display_map, display_map_multiplot, 
                   select_plot_params, filter_dataframe, 
                   get_params_map_acc_districts, get_params_map_acc_districts_weather)

from text import get_text

# Loading Analytical Resources
############################################################################

@st.cache_data # To save time and avoid long run time issues with the app
def load_resources():
    return pickle.load(open('resources/resources_web_app.pickle', 'rb'))

def convert_to_pandas(_acc_df):
    return _acc_df.to_pandas()

# loading the resources
resources_dict = load_resources()
acc_df = resources_dict['acc_df']
acc_df_pd = acc_df.to_pandas()
acc_not_people_df = resources_dict['acc_not_people_df']
people_dependent_variables = resources_dict['people_dependent_variables']
not_people_dependent_variables = resources_dict['not_people_dependent_variables']
columns_to_plot_people_dependent = resources_dict['columns_to_plot_people_dependent']
columns_to_plot_non_people_dependent_barplot = resources_dict['columns_to_plot_non_people_dependent_barplot'] 
columns_to_plot_non_people_dependent_histogram = resources_dict['columns_to_plot_non_people_dependent_histogram'] 
categories_order = resources_dict['categories_order']
num_acc_time_series = resources_dict['num_acc_time_series'] 
madrid_geojson = resources_dict['madrid_geojson']
districts_df = resources_dict['districts_df']
text = get_text()

############################################################################

st.title("Madrid Traffic Accidents")
st.header("Data Analysis")

st.image('images/logo8.png')


st.divider()

st.markdown(
"""
🚀 Welcome to the **Madrid Traffic Accidents Data Analysis App**, a powerful tool designed to provide insights into traffic incidents in Madrid. Leveraging data from the Madrid Open Data Portal, this app offers a comprehensive analysis to help you understand trends and patterns in road accidents across the city.

<div style="margin-top:30px;"></div>

🔭 **Goals**
- Enhance public awareness and inform policy-making for making Madrid's roads safer. 
- Whether you are a concerned citizen, a researcher, or a policymaker, this app provides valuable information at your fingertips.

 <div style="margin-top:30px;"></div>

💡**Features**
- **Conceptual Description of the Data**: in this section the data used is describe conceptually. If you want to know more about the data in which the analysis was based, visit this section.
- **Interactive Data Table**: explore detailed traffic accident records with the ability to filter and sort based on different criteria.
- **General Data Analysis**: gain insights through summary statistics and visualizations that highlight key trends and factors contributing to traffic accidents in Madrid.
- **Specific Data Analysis**: an analysis oriented to answer specific question is carried out in this section. The concrete questions can be found inside the section.
- **More in-depth Districts Data Analysis**: a more in-depth analysis regarding Madrid districts is done, keeping the focus on traffic accidents but including new variables to account for, making the analysis more flexible and enriching.
- **Data Download**: easily download the processed data for your own analysis or record-keeping.

<div style="margin-top:30px;"></div>

⚒️**Developers**
- This web application has been developed by ***Fabio Scielzo Ortiz***.
- Official GitHub repository of the app: [Madrid-Traffic-Accidents-App](https://github.com/FabioScielzoOrtiz/Madrid-Traffic-Accidents-App)

"""
, unsafe_allow_html=True
)

st.divider()

############################################################################
############################################################################

st.sidebar.image('images/logo1.jpg')
st.sidebar.header('Table of content')


############################################################################    

# TABLE WITH DATA

if st.sidebar.checkbox('Data conceptual description'):
    
    st.markdown('### Data conceptual description')

    st.markdown("""
    📋 The data was collected from [Portal Datos Abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=7c2843010d9c3610VgnVCM2000001f4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default)
    - Data from 2019 to 2024 was considered.
    - Conceptual details regarding the data can be found below, as well as in the cited page and the following [PDF](https://drive.google.com/file/d/1fCKCh2fZZH_jzNXPRsSV6CSGAZvuIUI3/view?usp=sharing).     
    - The original data have been pre-processed to obtain additional valuable resources from which to extract better insights.                      
       - *Feature engineering* was applied to gather new variables, what has allowed us to make a more enriching analysis.
    """)
    add_vertical_space(1)

    st.markdown(
        """
        <div style="background-color:#FFF3CD; border-left:6px solid #FFA726; padding:6px; border-radius:3px; font-size:16px;">
            ⚠️ Each observation (row/record) represent a person involved in a traffic accident in Madrid.
        </div>
        """,
        unsafe_allow_html=True
    )

    add_vertical_space(2)

    st.markdown('#### Variables Meaning')

    markdown_table = """
    | Variable Name | Description | Type |
    |---------------|-------------|------|
    | `num_expediente`    |  A unique identifier for each accident.  |   Identifier  | 
    | `fecha`    | Date in format dd/mm/yyyy. | Date  |  No analysis  |
    | `hora`   |   Time at which the accident occurred.     |  Date  |      
    | `localizacion`   | Street where the accident happened.   |  Categorical  |      
    | `numero`   |   Number of the street where the accident occurred, when it makes sense. |  Categorical  |      
    | `cod_distrito`   |  Code for `distrito`   |  Identifier  |      
    | `distrito`   |  Name of the district where the accident took place.   |  Categorical  |      
    | `tipo_accidente`   | The type of accident. |  Categorical  |      
    | `estado_meteorologico`   |  The weather conditions when the accident happened.   |  Categorical  |      
    | `tipo_vehiculo`   | The type of vehicle involved in the accident.  |  Categorical  |      
    | `tipo_persona`   |  The type of person involved in the accident.   |  Categorical  |      
    | `rango_edad`   |  The age range of the person involved in the accident. |  Categorical  |      
    | `sexo`   |  The biological sex of the person involved in the accident.   |  Categorical  |      
    | `cod_lesividad`   | Code for `lesividad`  |  Identifier  |      |
    | `lesividad`   |   Injury caused by the accident to the person involved.    |  Categorical  |      
    | `coordenada_x_utm`   |  Location for x-coordinate.    |  Quantitative  |      
    | `Coordenada_y_utm`   |  Location for y-coordinate.   |  Quantitative  |      
    | `positiva_alcohol`   | Whether or not the person involved in the accident tested positive for alcohol.  |  Categorical  |      
    | `positiva_droga`   |  Whether or not the person involved in the accident tested positive for drugs.  |  Categorical  |      
    """
    st.markdown(markdown_table)

    add_vertical_space(2)

    st.markdown('#### Feature Engineering')

    st.markdown("""
                The following variables have been created based on the original ones, process that is usually known as *feature engineering*.

                | Variable Name | Description | Type |
                |---------------|-------------|------|
                | `num_people_involved`    |  The number of people involved in an accident. Is the result of counting the number of records associated with the identifier (`num_expediente`) of that accident identifier.  |   Quantitative  |        
                | `year`    | Year of the accident. | Date  |      
                | `quarter`   | Quarter of the accident.     |  Date        
                | `month`   | Month of the accident.   |  Date  |      
                | `week`   |   Week of the accident. |  Date  |      
                | `weekday`   | Weekday of the accident.  |  Date  |     
                | `hour`   | Hour of the accident.  |  Date  |      
                | `phy_severity`   |  Severity of the physical consequences of the person involved in the accident. It was defined based on `lesividad` as follows: High severity if `lesividad` in ['Fallecido', 'Ingreso > 24h'], Medium severity if `lesividad` in ["Asist. inmediata CS", "Ingreso <= 24h"] and Low severity if `lesividad`in ["Asist. posterior CS", "Urg. sin ingreso", 'Asist. solo insitu', "Sin asist. sanitaria"].  |  Categorical  |     
                | `some_positive_involved`   | If there is any positive tested for drugs or alcohol among the involved people.  |  Categorical  |     
                | `some_death_involved`   |  If there is any death among the involved people    |  Categorical  |     
                | `severe_accident`   | Whether the accident is severe  or not. And accident is considered severe if there is at least one person involved with high severity physical consequences.  |  Identifier  |      
                | `old_driver_involved`   |  If there is at least one old driver involved in the accident.   |  Categorical  |     
                | `only_old_driver_involved`   |  If all the drivers involved in the accident are old.   |  Categorical  |      
                | `young_driver_involved`   |  If there is at least one young driver involved in the accident.    |  Categorical  |     
                | `only_young_driver_involved`   |  If all the drivers involved in the accident are young.    |  Categorical  |     
                | `female_driver_involved`   | If there is at least one female driver involved in the accident.     |  Categorical  |     
                | `only_female_driver_involved`   |  If all the drivers involved in the accident are female.  |  Categorical  |     
                | `male_driver_involved`   |  If there is at least one male driver involved in the accident.    |  Categorical  |     
                | `only_male_driver_involved`   |  If all the drivers involved in the accident are male.  |  Categorical  |     
                | `positive_driver_involved`   | If there is at least one positive tested driver involved in the accident.    |  Categorical  |     
                """)
    
    add_vertical_space(2)

    st.markdown("""
                - It\'s important to highlight that the most part of the above variables are referred to accidents, and this made possible the creation of a new data table was built, in which each row/record represent an accident.
                - Besides, a dictionary `num_acc_time_series` was generated with the time series of number of accidents for different periodicity: year, quarter, month, week, day, hour, year-quarter, year-month, year-month-day.
                
                - In addition, data regarding the districts has been both created from the above and collected from other sources in [Madrid Datos Abiertos](https://datos.madrid.es/portal/site/egob).
                   The aim is to make a more in-depth and exhaustive analysis about the traffic accidents on Madrid depending on the districts.
               
                    The following table contains the variables include in the referred districts data table, in which rows/records represent Madrid districts.

                    | Variable Name | Description | Type |
                    |---------------|-------------|------|        
                    | `num_accidents`   |  Number of traffic accidents in the district.  |  Quantitative  |     
                    | `num_severe_accident`   |  Number of severe traffic accidents in the district.   |  Quantitative  |     
                    | `poblacion`   |  Population of the district.   |  Quantitative  |     
                    | `perc_poblacion_extranjera`   |  Percentage of the district population that is foreign.  |  Quantitative  |     
                    | `intervenciones_policiales_con_detenidos`   |  Police interventions with arrests in the district.   |  Quantitative  |     
                    | `% de 0 a 15 años`   |  Percentage of population of the district with an age between 0 and 15 years.   |  Quantitative  |     
                    | `% de 16 a 64 años`   |  Percentage of population of the district with an age between 16 and 64 years.   |  Quantitative  |     
                    | `% de 65 años y más`   |  Percentage of population of the district with an age higher or equal to 65  years.   |  Quantitative  |     
                    | `% de 80 años y más`   |  Percentage of population of the district with an age higher or equal to 80 years.   |  Quantitative  |     
                    | `renta_media_persona`   |  Average disposable income per person in the district.   |  Quantitative  |     
                    | `detenidos_mil_hab`   |  Arrested per 1000 inhabitants in the district.   |  Quantitative  |     
                    | `acc_mil_hab`   |  Traffic accidents per 1000 inhabitants in the district.  |  Quantitative  |     
                    | `severe_acc_mil_hab`   |  Severe traffic accidents per 1000 inhabitants in the district.   |  Quantitative  |    
                """)
    
    add_vertical_space(1)
    st.markdown('🔭 Finally, the complete data was processed and analyzed in a smart way to obtain significant conclusions regarding Madrid traffic accidents.')


    st.divider()

############################################################################    

# TABLE WITH DATA

if st.sidebar.checkbox('Table with the data'):
    
    st.markdown('### Table with the data')
    
    filtered_df = filter_dataframe(acc_df.to_pandas())
    st.dataframe(filtered_df)
    st.write("<div style='font-size:14px; text-align:left'>Number of rows:  {}</span></div>".format(filtered_df.shape[0]), unsafe_allow_html=True)
    st.write("<div style='font-size:14px; text-align:left'>Number of columns:   {}</span></div>".format(filtered_df.shape[1]), unsafe_allow_html=True)

    st.divider()

############################################################################

# GENERAL DATA ANALYSIS 

if st.sidebar.checkbox('General Data Analysis', key='data_analysis_checkbox'):

    st.markdown('### General Data Analysis')
    
    st.markdown("<p style='font-size:18px; margin-bottom:-90px'>Select Analysis Type:</p>", unsafe_allow_html=True)
    analysis_type = st.selectbox(
                                    " ",
                                    ("Descriptive Summary", "Frequency Tables", "Visualization"),
                                    key='analysis_type_selectbox'
                                )
    st.divider()
    
    if analysis_type == "Descriptive Summary":
        selected_variables = multi_selector(options_list = people_dependent_variables + not_people_dependent_variables, title='Select a variable:', key='variables_multiselector')
        display_descriptive_summary(acc_df, acc_not_people_df, people_dependent_variables, not_people_dependent_variables, selected_variables)

    elif analysis_type == "Frequency Tables":
        selected_variables = multi_selector(options_list = people_dependent_variables + not_people_dependent_variables, title='Select a variable:', key='variables_multiselector')
        #display_frequency_tables(acc_df, acc_not_people_df, people_dependent_variables, not_people_dependent_variables, selected_variables)

    elif analysis_type == 'Visualization':
        st.markdown("<p style='font-size:18px; margin-bottom:-90px'>Select Visualization Type:</p>", unsafe_allow_html=True)
        viz_type = st.selectbox(
                                    " ",
                                    #("Select All", "Barplot", "Histogram", "Lineplot"),
                                    ("Barplot", "Histogram"),
                                    key='visualization_type_selectbox',
                                    index = 0 # default = "Barplot"
                                )
        
        st.markdown(
            """
            <div style="background-color:#FFF3CD; border-left:5px solid #FFA726; padding:6px; border-radius:3px; font-size:14px;">
                ⚠️ Statistics are computed over the records without missing values for the considered variable.
                <br><br>
                Example: <code>lesividad</code> has a 45.41% of missing values, so its statistics are computed excluding these missing records.
            </div>
            """,
            unsafe_allow_html=True
        )

        add_vertical_space(2)

        if viz_type == 'Barplot':

            selected_variables = multi_selector(options_list = columns_to_plot_people_dependent + columns_to_plot_non_people_dependent_barplot,
                                                  title='Select a variable:', key='variables_multiselector')
            for i, col in enumerate(selected_variables):
                st.divider()
                figsize, orientation, color = select_plot_params(key_id=f'0{i}', options=['figsize', 'orientation', 'color'])
                if col in columns_to_plot_people_dependent:
                    display_barplot(X=acc_df[col], figsize=figsize, color=color, orientation=orientation,
                                    categories_order=categories_order[col], title=text['plot_titles'][viz_type][col]
                                   )
                elif col in columns_to_plot_non_people_dependent_barplot:
                    display_barplot(X=acc_not_people_df[col], figsize=figsize, color=color, orientation=orientation,
                                    title=text['plot_titles'][viz_type][col]
                                   )
                try:
                    st.markdown(text['analysis'][viz_type][col])
                except:
                    pass
        
        elif viz_type == 'Histogram':

            selected_variables = multi_selector(options_list=columns_to_plot_non_people_dependent_histogram, title='Select a variable:', key='variables_multiselector')
            for i, col in enumerate(selected_variables):
                st.divider()
                figsize, n_bins, color = select_plot_params(key_id=f'0{i}', options=['figsize', 'nbins', 'color'])
                display_histogram(X=acc_not_people_df[col], figsize=figsize, color=color, nbins=n_bins, 
                                  title=text['plot_titles'][viz_type][col]
                                 )
                try:
                    st.markdown(text['analysis'][viz_type][col])
                except:
                    pass

        #elif viz_type == 'Lineplot':
        #    selected_periods = multi_selector(options_list=list(num_acc_time_series.keys()), title='Select a periodicity:')
        #    for i, period in enumerate(selected_periods):
        #        st.divider()
        #        figsize, nxticks, line_width, color = select_plot_params(key_id=i, options=['figsize', 'nxticks', 'line_width', 'color'])
        #        display_lineplot(df=num_acc_time_series[period], x=period, y='num_accidents', figsize=figsize, color=color,
        #                         num_xticks=nxticks, line_width=line_width, title=None, #title=plot_titles[viz_type][period]
        #                        )
        #        st.markdown(text['analysis'][viz_type][period])

        #elif viz_type == 'Select All':
            #st.write('TO DO  ')
            #text['analysis'][viz_type][col]

        st.divider()

############################################################################

if st.sidebar.checkbox('Specific Data Analysis'):
    
    st.markdown('### Specific Data Analysis')

    st.markdown("<p style='font-size:18px; margin-bottom:-90px'>Select Analysis Type:</p>", unsafe_allow_html=True)
    analysis_type_dict = {'acc_periods': "Which periods have more affluence of accidents?", 
                          'acc_districts': "Which Madrid districts have more affluence of accidents?",
                          'acc_districts_weather':"Given a weather condition, which districts have more accidents affluence?",
                          'sev_acc~positive':"Which is the influence of drugs and alcohol on the probability of having a severity accident?",
                          'sev_acc~weather':"Which is the influence of weather conditions on the probability of having a severity accident?", 
                          'sev_acc~age':"Which is the influence of age on the probability of having a severity accident?",
                          'sev_acc~sex':"Which is the influence of sex on the probability of having a severity accident?",
                          'sev_acc~districts':"Which is the influence of districts on the probability of having a severity accident?",
                          'phy_sev~age': "Which is the influence of age on suffering severe physical consequences in an accident?",
                          }
    analysis_type_tuple = tuple(x for x in analysis_type_dict.values())
    analysis_type = st.selectbox(
                                    " ",
                                    analysis_type_tuple,
                                    key='specific_analysis_type_selectbox'
                                )
    #st.divider()
    
    if analysis_type == analysis_type_dict['acc_periods']: # accidents ~ periods
      
        selected_periods = multi_selector(options_list=list(num_acc_time_series.keys()), title='Select a periodicity:', key='periodicity_multiselect')
        if len(selected_periods) == len(list(num_acc_time_series.keys())): # 'Select All' is selected
            st.divider()
            line_width, color = select_plot_params(key_id=f'1_', options=['line_width', 'color'])
            display_time_series_multiplot(dic_df=num_acc_time_series, y='num_accidents', color=color, line_width=line_width,
                                          title=text['plot_titles']['Lineplot']['multiplot'])
        for i, period in enumerate(selected_periods):
            st.divider()
            figsize, nxticks, line_width, color = select_plot_params(key_id=f'1{i}', options=['figsize', 'nxticks', 'line_width', 'color'])
            display_lineplot(df=num_acc_time_series[period], x=period, y='num_accidents', figsize=figsize, color=color,
                                num_xticks=nxticks, line_width=line_width, title=text['plot_titles']['Lineplot'][period]
                            )
            st.markdown(text['analysis']['Lineplot'][period])

    ####################################################

    elif analysis_type == analysis_type_dict['acc_districts']: # accidents ~ districts
        
        colorscale = select_plot_params(key_id='acc_districts', options=['colorscale'])
        df = resources_dict['acc_districts']
        locations, z_dict, subtitles, hue_titles = get_params_map_acc_districts(df)
        display_map_multiplot(geojson=madrid_geojson, locations=locations, z_dict=z_dict, 
                              title='<b>Madrid Traffic Accidents by Districts (2019-2024)</b>', 
                              subtitles=text['plot_titles']['acc_districts'], 
                              hue_titles=text['hue_titles']['acc_districts'],
                              hue_vspace=0.25, width=750, title_height=0.93, 
                              subtitle_size=17, subtitles_height=0.93, colorscale=colorscale)
        
        st.markdown(text['analysis']['acc_districts'])
        st.divider()
        
        st.markdown(f"<p style='font-size:17px; margin-bottom:-100px'>Display the maps individually?</p>", unsafe_allow_html=True)
        decision = st.selectbox(' ', ['No', 'Yes'], key=f'display_individual_selectbox')
        add_vertical_space(2)
        if decision == 'Yes':           
            for key in z_dict.keys(): 
                display_map(geojson=madrid_geojson, locations=locations, z=z_dict[key], colorscale=colorscale,
                            title=text['plot_titles']['acc_districts'][key] + ' by Districts (2019-2024)', 
                            hue_title=text['hue_titles']['acc_districts'][key], title_size=14)             

    ####################################################

    #elif analysis_type == analysis_type_dict['sev_acc_districts']: # distribution severe acc by districts

    #    df = resources_dict['sev_acc_districts']

    #    display_map(geojson=madrid_geojson, locations=df['distrito'], z=df['perc_severe_acc'], 
    #                title='<b>Distribution of Severe Accidents by District (2019-2024)</b>',
    #                hue_title='Percentage Severe Accident (%)', title_size=13.5)

    #    st.markdown(text['analysis']['sev_acc_districts'])

    ####################################################

    elif analysis_type == analysis_type_dict['sev_acc~positive']: # severe accidents ~ positive drugs or alcohol driver 
        
        figsize, color = select_plot_params(key_id=f'positive_severe_acc', options=['figsize', 'color'])
        df = resources_dict['sev_acc~positive']
        display_barplot_2D(df, x='positive_driver_involved', y='severe_accident', 
                           ylabel='Probability Severe Accident (%)', xlabel='Positive Driver Involved',
                           title='<b>P(Severe Accident | Positive Driver Involved)</b>', color=color, figsize=figsize,
                           y_grid_color='lightgrey', x_grid_color='white')

        st.markdown(text['analysis']['sev_acc~positive'])

    ####################################################

    elif analysis_type == analysis_type_dict['sev_acc~weather']: # accidents ~ weather conditions
      
        figsize, color = select_plot_params(key_id=f'estado_meteo_severe_acc', options=['figsize', 'color'])
        df = resources_dict['sev_acc~weather']
        display_barplot_2D(df, x='estado_meteorológico', y='perc_severe_acc', 
                           ylabel='Probability Severe Accident (%)',
                           xlabel='estado_meteorológico',
                           title='<b>P(Severe Accident | Weather conditions)</b>',
                           figsize=figsize, color=color, y_grid_color='lightgrey', x_grid_color='white')
        
        st.markdown(text['analysis']['sev_acc~weather'])

    ####################################################

    elif analysis_type == analysis_type_dict['sev_acc~age']: # accidents ~ driver age

        figsize, color = select_plot_params(key_id=f'age_severe_acc', options=['figsize', 'color'])
        df = resources_dict['sev_acc~age']
        for key in df.keys():
            display_barplot_2D(df[key], x=key, y='perc_severe_acc', 
                               ylabel='Probability Severe Accident (%)',
                               xlabel=key,
                               title=f"<b>P(Severe Accident | {' '.join(word.capitalize() for word in key.split('_'))})</b>",
                               figsize=figsize, color=color, y_grid_color='lightgrey', x_grid_color='white')
            st.markdown(text['analysis']['sev_acc~age'][key])
            st.divider()

    ####################################################

    elif analysis_type == analysis_type_dict['sev_acc~sex']: # accidents ~ driver sex

        figsize, color = select_plot_params(key_id=f'sex_severe_acc', options=['figsize', 'color'])
        df = resources_dict['sev_acc~sex']
        for key in df.keys():
            display_barplot_2D(df[key], x=key, y='perc_severe_acc', 
                               ylabel='Probability Severe Accident (%)',
                               xlabel=key,
                               title=f"<b>P(Severe Accident | {' '.join(word.capitalize() for word in key.split('_'))})</b>",
                               figsize=figsize, color=color, y_grid_color='lightgrey', x_grid_color='white')
            st.markdown(text['analysis']['sev_acc~sex'][key])
            st.divider()

    ####################################################

    elif analysis_type == analysis_type_dict['sev_acc~districts']: # severe accidents ~ district

        colorscale = select_plot_params(key_id='sev_acc~districts', options=['colorscale'])
        df = resources_dict['sev_acc~districts']
        display_map(geojson=madrid_geojson, locations=df['distrito'], z=df['perc_severe_acc'], 
                    title='<b>Probability of Severe Accidents by District (2019-2024)</b>',
                    hue_title='Probability Severe Accident (%)', title_size=13.5, colorscale=colorscale)

        st.markdown(text['analysis']['sev_acc~districts'])

    ####################################################

    elif analysis_type == analysis_type_dict['acc_districts_weather']: # severe accidents ~ district

        colorscale = select_plot_params(key_id='acc_districts_weather', options=['colorscale'])
        df = resources_dict['acc_districts_weather']
        locations, z_dict, subtitles, hue_titles = get_params_map_acc_districts_weather(df)  
        display_map_multiplot(geojson=madrid_geojson, locations=locations, z_dict=z_dict, 
                              title='<b>Madrid Traffic Accidents by Districts and Weather Conditions (2019-2024)</b>', 
                              subtitles=subtitles, 
                              hue_titles=hue_titles, colorscale=colorscale,
                              mapbox_zoom=8.5, title_size=13, subtitles_height=0.965, hspace=0.04,
                              subtitle_size=17, title_height=0.965, width=750, height=1000,
                              hue_height=0.82, hue_vspace=0.15)

        st.markdown(text['analysis']['acc_districts_weather'])

        st.markdown(f"<p style='font-size:17px; margin-bottom:-100px'>Display another visualization?</p>", unsafe_allow_html=True)
        decision = st.selectbox(' ', ['No', 'Yes'], key=f'display_another_selectbox')
        add_vertical_space(2)
        if decision == 'Yes':   
            display_barplot_2D_multiplot(df=df, y='estado_meteorológico', x='distrito', 
                                         xlabel='Percentage of acidents', 
                                         title='<b>Madrid Traffic Accidents by Districts and Weather Conditions</b>',
                                         figsize=(660,900))  

    elif analysis_type == analysis_type_dict['phy_sev~age']: # phy_consequence = High ~ age

        figsize, color = select_plot_params(key_id=f'estado_meteo_severe_acc', options=['figsize', 'color'])
        df = resources_dict['phy_sev~age']
        display_barplot_2D(df, x='age_category', y='perc_people_acc', 
                           title='<b>P(High Severity Physical Consequences | Age Category)</b>', 
                           ylabel='Probability High Severity Physical Consequences (%)',
                           xlabel='Age Category',
                           figsize=figsize, color=color, y_grid_color='lightgrey', x_grid_color='white',
                           xlabel_size=15, ylabel_size=14)
        
        st.markdown(text['analysis']['phy_sev~age'])

############################################################################

if st.sidebar.checkbox('More in-depth Districts Data Analysis'):
    
    st.markdown('### More in-depth Districts Data Analysis')
            
    districts_df = districts_df.to_pandas()
    options_to_remove = ['distrito', 'poblacion_española', 'poblacion_extranjera', 'Edad promedio', 'perc_acc', 'perc_sec_acc']
    options = [x for x in districts_df.columns.to_list() if x not in options_to_remove]

    col1, col2, col3 = st.columns(3)
    with col1:
        y = st.selectbox('Select y:', options, key='more_districts_y_selectbox')
    with col2:
        x = st.selectbox('Select x:', options, index=2, key='more_districts_x_selectbox')
    with col3:
        z = st.selectbox('Select z (optional):', [None] + options, key='more_districts_z_selectbox')
            
    figsize, colorscale, color = select_plot_params(key_id='more_districts', options=['figsize', 'colorscale', 'color'])
    title = f'<b>{y} vs {x} vs {z}</b>' if z != None else f'<b>{y} vs {x}</b>'
    display_scatterplot(df=districts_df, x=x, y=y, z=z, point_labels='distrito', 
                        figsize=figsize, title=title, color=color, colorscale=colorscale)  
    try:
        text['analysis'][f'{x}~{y}']
    except: 
        try:
            text['analysis'][f'{y}~{x}']
        except:
            pass         

    st.divider()

############################################################################

# DOWNLOAD DATA AS CSV

if st.sidebar.checkbox('Download Data'):

    st.subheader('Download Data')

    st.markdown('The original data is available in the following link of the web portal [Madrid datos abiertos](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=7c2843010d9c3610VgnVCM2000001f4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default).')
    st.markdown('But here you can download a preprocessed version of the original one, used along this project.')
    csv = acc_df_pd.to_csv(index=False)
    # Use st.download_button for a proper download button
    st.download_button(
        label='Download CSV',
        data=csv,
        file_name='madrid_traffic_accidents.csv',
        mime='text/csv',
        key='download_button',
        type='primary'
    )

    st.divider()

#####################################################################################################################################


st.markdown("Visit our personal website to learn more about our work and other projects ➡️ [Estadistica4all](https://estadistica4all.com/).", unsafe_allow_html=True)
st.markdown('⚙️ Developed by ***Fabio Scielzo Ortiz***.')


    