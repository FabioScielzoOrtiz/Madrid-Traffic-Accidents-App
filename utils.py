
import polars as pl 
import pandas as pd
import numpy as np
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from pandas.api.types import (is_categorical_dtype, is_datetime64_any_dtype,
                              is_numeric_dtype, is_object_dtype)

from BigEDA.descriptive import summary, freq_table
from BigEDA.plots import (barplot_interactive, histogram_interactive, lineplot_interactive, scatterplot_interactive,
                          time_series_interactive_multiplot, map_interactive, map_interactive_multiplot, 
                          barplot_interactive_2D, barplot_interactive_2D_multiplot)

############################################################################################################################################
# GENERAL ANALYSIS UTILS
############################################################################################################################################

# Widget for selecting variables in General Analysis section
def multi_selector(options_list, title, key):
    
    st.markdown(f"<p style='font-size:18px; margin-bottom:-90px'>{title}</p>", unsafe_allow_html=True)
    selected_options = st.multiselect(
        " ",
        options=["Select All"] + options_list,
        default=["Select All"],
        key=key
    )  
    # Filter variables based on selection
    if "Select All" in selected_options:
        selected_options = options_list

    return selected_options

##########################################################################################################

# Function to display Descriptive Summary in the General Analysis section
def display_descriptive_summary(acc_df, acc_not_people_df, people_dependent_variables, not_people_dependent_variables, selected_variables):

    st.markdown('#### Descriptive Summary')

    # Filtering by selected variables
    people_dependent_variables = [col for col in people_dependent_variables if col in selected_variables]
    not_people_dependent_variables = [col for col in not_people_dependent_variables if col in selected_variables]

    # Compute descriptive summaries
    _, cat_summary_1 = summary(df=acc_df, quant_col_names=[],
                               cat_col_names=people_dependent_variables)
    quant_summary_2, cat_summary_2 = summary(df=acc_not_people_df, auto_col=False,
                                        quant_col_names=['num_people_involved'],
                                        cat_col_names=[x for x in not_people_dependent_variables if x != 'num_people_involved'])
    try:
        cat_summary = pd.concat([cat_summary_1, cat_summary_2], axis=0)
    except:
        cat_summary = None
    # Printing the output as a data-frame
    st.markdown('Descriptive summary for the categorical variables')
    st.dataframe(cat_summary)
    st.markdown('Descriptive summary for the quantitative variables')
    st.dataframe(quant_summary_2)
    # Set a visual division
    st.divider()

##########################################################################################################

# Function to display Frequency Tables in the General Analysis section
def display_frequency_tables(acc_df, acc_not_people_df, people_dependent_variables, not_people_dependent_variables, selected_variables):

    st.markdown('#### Frequency tables')

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

    # Filtering by selected variables
    people_dependent_variables = [col for col in people_dependent_variables if col in selected_variables]
    not_people_dependent_variables = [col for col in not_people_dependent_variables if col in selected_variables]

    for col in people_dependent_variables:
        #st.markdown("<br>", unsafe_allow_html=True)
        st.divider()
        st.markdown(f'**Frequency table for `{col}`**')
        acc_df_dropped_nulls = acc_df.drop_nulls(subset=col)
        freq_table_output = freq_table(X=acc_df_dropped_nulls[col])
        st.dataframe(freq_table_output)
        st.markdown(f"<p style='font-size:13px'>Number of unique values (rows): {freq_table_output.shape[0]}</p>", unsafe_allow_html=True)

    for col in not_people_dependent_variables:
        #st.markdown("<br>", unsafe_allow_html=True)
        st.divider()
        st.markdown(f'**Frequency table for `{col}`**')
        acc_not_people_df_dropped_nulls = acc_not_people_df.drop_nulls(subset=col)
        freq_table_output = freq_table(X=acc_not_people_df_dropped_nulls[col])
        st.dataframe(freq_table_output)
        st.markdown(f"<p style='font-size:13px'>Number of unique values (rows): {freq_table_output.shape[0]}</p>", unsafe_allow_html=True)
    
##########################################################################################################

# Function to display Barplot in the web-app
def display_barplot(X, figsize, color='tomato', categories_order=None, title=None, orientation='h'):
  
    fig = barplot_interactive(X=X, figsize=figsize, font_family='Comic Sans MS', color=color, title=title,
                              categories_order=categories_order, margin_l=50, margin_r=50, margin_t=80, margin_b=50,
                              title_width=0.5, title_height=1.15, title_size=17, orientation=orientation, 
                              xlabel_size=17, ylabel_size=17, xticks_size=14, yticks_size=14)
    
    st.plotly_chart(fig, theme=None, use_container_width=True) # Display the figure

##########################################################################################################

# Function to display Barplot in the web-app
def display_barplot_2D(df, x, y, ylabel, xlabel, color, title, figsize, x_grid_color='lightgrey', y_grid_color='white',
                       xlabel_size=15, ylabel_size=16):
  
    fig = barplot_interactive_2D(df=df, x=x, y=y, ylabel=ylabel, xlabel=xlabel,
                                 title=title, figsize=figsize, font_family='Comic Sans MS', 
                                 xlabel_size=xlabel_size, ylabel_size=ylabel_size, xticks_size=16, yticks_size=14, 
                                 color=color, margin_l=50, margin_r=40, margin_t=60, margin_b=50, 
                                 title_size=17, title_width=0.5, title_height=1.1, 
                                 y_grid_color=y_grid_color, x_grid_color=x_grid_color)
    
    st.plotly_chart(fig, theme=None, use_container_width=True) # Display the figure

##########################################################################################################

def display_barplot_2D_multiplot(df, x, y, xlabel, title, figsize):
  
    fig = barplot_interactive_2D_multiplot(df=df, y=y, x=x, xlabel=xlabel,
                                            figsize=figsize, font_family='Comic Sans MS', title=title,
                                            xlabel_size=13, ylabel_size=14, xticks_size=12, yticks_size=12, 
                                            margin_l=50, margin_r=40, margin_t=60, margin_b=50, 
                                            title_size=17, title_width=0.5, title_height=1.09,
                                            subtitle_size=15, wspace=0.3, hspace=0.09)
       
    st.plotly_chart(fig, theme=None, use_container_width=False) # Display the figure

##########################################################################################################

# Function to display Histogram in the web-app
def display_histogram(X, figsize, color='tomato', nbins=30, title=None):
  
    fig = histogram_interactive(X=X, figsize=figsize, color=color, nbins=nbins, title=title,
                                font_family='Comic Sans MS', title_size=17, 
                                xlabel_size=16, ylabel_size=16, xticks_size=13, yticks_size=13, 
                                margin_l=50, margin_r=40, margin_t=80, margin_b=50, 
                                title_width=0.5, title_height=1.15)
    
    st.plotly_chart(fig, theme=None, use_container_width=True) # Display the figure

##########################################################################################################

# Function to display Lineplot in the web-app
def display_lineplot(df, x, y, figsize, color, num_xticks, line_width, title):

    fig = lineplot_interactive(df, x, y, figsize=figsize, font_family='Comic Sans MS', title=title,
                         xlabel_size=16, ylabel_size=16, xticks_size=13, yticks_size=13, 
                         color=color, margin_l=50, margin_r=40, margin_t=80, margin_b=50, 
                         title_size=12, title_width=0.5, title_height=0.91,
                         num_xticks=num_xticks, line_width=line_width)
    
    st.plotly_chart(fig, theme=None, use_container_width=True)

##########################################################################################################

# Function to display Scatterplot in the web-app
def display_scatterplot(df, x, y, z, point_labels, figsize, color, title, colorscale):

    fig = scatterplot_interactive(df=df, x=x, y=y, figsize=figsize, 
                                  z_size=z, z_color=z, point_labels=point_labels, point_labels_size=13,
                                  font_family='Comic Sans MS', xlabel=None, xlabel_size=16.5, 
                                  ylabel_size=16.5, xticks_size=12, yticks_size=12, colorscale=colorscale,
                                  color=color, point_size=15, legend_title_side='right',
                                  margin_l=50, margin_r=40, margin_t=60, margin_b=50, 
                                  title=title, title_size=18, title_width=0.5, title_height=1.095)
    
    st.plotly_chart(fig, theme=None, use_container_width=True)

##########################################################################################################

# Function to display Histogram in the web-app
def display_time_series_multiplot(dic_df, y, color, line_width, title):

    nxticks = {}
    nxticks['year'] = 6
    nxticks['quarter'] = 4
    nxticks['month'] = 12
    nxticks['week'] = 25
    nxticks['day'] = 25
    nxticks['hour'] = 15
    nxticks['year-quarter'] = 5
    nxticks['year-month'] = 7
    nxticks['year-month-day'] = 6
    nxticks['weekday'] = 7
    periods = nxticks.keys()
    angle_periods = ['year-month', 'year-month-day', 'weekday']
    non_angle_periods = [x for x in periods if x not in angle_periods]
    tickangle = {period: 0 for period in non_angle_periods}
    tickangle.update({period: 20 for period in angle_periods})

    fig = time_series_interactive_multiplot(dic_df, y=y, figsize=(1000,1100), 
                               font_family='Comic Sans MS', xlabel_size=12, ylabel_size=12, 
                               xticks_size=10, yticks_size=10, line_width=line_width, nxticks=nxticks,
                               n_cols=2, wspace=0.1, hspace=0.1, subtitle_size=16, tickangle=tickangle,
                               margin_l=50, margin_r=40, margin_t=120, margin_b=60, color=color,
                               title=title, title_size=16.5, title_width=0.5, title_height=1.1)
    
    st.plotly_chart(fig, theme=None, use_container_width=True)

##########################################################################################################

def display_map(geojson, locations, z, title, hue_title, colorscale, title_size=14):

    fig = map_interactive(geojson=geojson, locations=locations, z=z, 
                          featureidkey="properties.name", marker_opacity=0.7, marker_line_width=1.25, 
                          mapbox_zoom=9, mapbox_center={"lat": 40.45, "lon": -3.7038}, 
                          title=title, title_size=title_size, title_height=0.93, title_width=0.47, hue_title=hue_title,
                          width=950, height=500, margin_t=70, colorscale=colorscale)

    st.plotly_chart(fig, theme=None, use_container_width=True)

##########################################################################################################

def display_map_multiplot(geojson, locations, z_dict, title, subtitles, hue_titles, colorscale,
                          mapbox_zoom=8.6, title_size=14, subtitles_height=0.94, hspace=0.08,
                          subtitle_size=16.5, title_height=0.95,  width=730, height=710,
                          hue_height=0.8, hue_vspace=0.2):

    # Define the colorscale
    fig = map_interactive_multiplot(geojson=geojson, locations=locations, z_dict=z_dict, title=title, subtitles=subtitles, hue_titles=hue_titles,  
                                    n_cols=2, featureidkey="properties.name", colorscale=colorscale, marker_opacity=0.7, marker_line_width=1.25,
                                    mapbox_zoom=mapbox_zoom, mapbox_center={"lat": 40.45, "lon": -3.7038}, title_size=title_size, subtitle_size=subtitle_size, 
                                    title_height=title_height, title_width=0.5, width=width, height=height, font_family='Comic Sans MS', 
                                    margin_l=50, margin_r=50, margin_t=65, margin_b=40,
                                    hspace=hspace, wspace=0, subtitles_height=subtitles_height, hue_height=hue_height, hue_vspace=hue_vspace)

    st.plotly_chart(fig, theme=None, use_container_width=False)

##########################################################################################################

def figsize_widget(key_id):
        fig_height = st.slider('Height', min_value=0, max_value=800, value=500, step=50, key=f'fig_height_slider_{key_id}')
        fig_width = None
        figsize = (fig_width, fig_height)
        return figsize

def orientation_widget(key_id):
    orientation = st.selectbox('Orientation', ['h', 'v'], key=f'orientation_selectbox_{key_id}')
    return orientation

def nbins_widget(key_id):
    n_bins = st.slider('Bins', min_value=5, max_value=60, value=25, step=1, key=f'bins_slider_{key_id}')
    return n_bins

def color_widget(key_id):
    color = st.color_picker('Color', '#ECA445', key=f'color_picker_{key_id}')  # Default color is tomato
    return color

def colorscale_widget(key_id):
    color = st.selectbox('Colorscale', ['purples', 'reds', 'blues', 'magenta', 'viridis'], key=f'orientation_selectbox_{key_id}')
    return color

def nxticks_widget(key_id):
    nxticks = st.slider('Num. x-ticks', min_value=1, max_value=25, value=6, step=1, key=f'nxticks_slider_{key_id}')  # Default color is tomato
    return nxticks

def line_width_widget(key_id):
    line_width = st.slider('Line width', min_value=1, max_value=10, value=3, step=1, key=f'line_width_slider_{key_id}')  # Default color is tomato
    return line_width

param_plot_widget = {}
param_plot_widget['figsize'] = figsize_widget 
param_plot_widget['orientation'] = orientation_widget 
param_plot_widget['nbins'] = nbins_widget 
param_plot_widget['color'] = color_widget 
param_plot_widget['colorscale'] = colorscale_widget 
param_plot_widget['nxticks'] = nxticks_widget
param_plot_widget['line_width'] = line_width_widget


def select_plot_params(key_id, options=['figsize', 'color', 'nbins', 'nxticks', 'line_width']):
    
    # key_id: an id for the widget key that allows running the function inside a loop avoiding 'DuplicateWidgetID' error
   
    st.markdown("<p style='font-size:17px; margin-bottom:-10px'>Select plot parameters:</p>", unsafe_allow_html=True)
    
    cols = st.columns(len(options))
    return_list = []
    for i, param in enumerate(options):
        with cols[i]:
            return_list.append(param_plot_widget[param](key_id))

    if len(return_list) == 1:
        return return_list[0]
    else:
        return return_list

##########################################################################################################

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters if you want 👇")

    if not modify:
        return df

    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        #if is_object_dtype(df[col]):
        #    try:
        #        df[col] = pd.to_datetime(df[col])
        #    except Exception:
        #        pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on variables:", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 50:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    _min,
                    _max,
                    (_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].str.contains(user_text_input)]

    return df

##############################################################################

def get_params_map_acc_districts(df):
        
    locations = df['accidents']['distrito']
    z_dict, subtitles, hue_titles = {}, {}, {}
    z_dict['accidents'] = df['accidents']['percentage']
    z_dict['severe_accidents'] = df['severe_accidents']['percentage']
    z_dict['acc_1000_hab'] = df['acc_1000_hab']['accidentes por mil hab']
    z_dict['severe_acc_1000_hab'] = df['severe_acc_1000_hab']['accidentes severos por mil hab']
    
    return locations, z_dict, subtitles, hue_titles

##############################################################################

def get_params_map_acc_districts_weather(df):

    distritos = pl.DataFrame(df['distrito'].drop_nulls().unique())
    estados_metereologicos = ['Despejado', 'Nublado', 'Lluvia débil', 'LLuvia intensa', 'Nevando', 'Granizando'] 
    df_map, z_dict, subtitles, hue_titles = {}, {}, {}, {}
    for i, estado in enumerate(estados_metereologicos):
        df_map[estado] = df.filter(pl.col('estado_meteorológico') == estado).join(distritos, on='distrito', how='outer')\
                                .with_columns(pl.col('percentage').fill_null(0)).select(['distrito_right', 'percentage'])\
                                .rename({'distrito_right': 'distrito'})
        z_dict[estado] = df_map[estado]['percentage']
        subtitles[estado] = estado
        hue_titles[estado] = 'Perc. of accidents' if i == int(len(estados_metereologicos)/2) - 1 else ''
    locations = df_map[estado]['distrito'] 

    return locations, z_dict, subtitles, hue_titles

##############################################################################