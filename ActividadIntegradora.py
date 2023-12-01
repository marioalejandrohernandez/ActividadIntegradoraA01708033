import streamlit as st
import pandas as pd
import numpy as np
import plotly as px
import plotly.figure_factory as ff
from bokeh.plotting import figure
import matplotlib.pyplot as plt


##Cambios 
#1-Se le cambio el estilo al titulo del dashboard para que sea tetrico


#2- Se le agrego una grafica de pie para ver el codigo de reporte 


#3- Se agrego una grafica de barras para ver los delitos cometidos por año 

#4-Se le agrego un filtro para ver "Report Typ Description"

#-5 Se pusieron 4  graficas en dos columnas para que esten juntas 

#-6 Se le agrego un filtro para ver "Year "

#-7 Se amplio el df de mapa para tener mas filtos 



st.markdown(
    '<h1 style="color: red; font-family: Chiller, sans-serif;">Police Incident Reports from 2018 to 2020 in San Francisco</h1>',
    unsafe_allow_html=True
)

df = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present (1).csv") 
st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')
mapa = pd.DataFrame()

mapa['Date'] = df['Incident Day of Week']
mapa['Day'] = df['Incident Day of Week']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Incident Subcategory'] = df['Incident Subcategory']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa['Report Type Description'] = df['Report Type Description']
mapa['Incident Subcategory']= df['Incident Subcategory']
mapa['Report Type Code'] = df['Report Type Code']
mapa['Incident Year'] = df['Incident Year']
mapa = mapa.dropna()

subset_data2 = mapa
police_district_input = st.sidebar.multiselect(
'Police District',
mapa.groupby('Police District').count().reset_index()['Police District'].tolist())
if len(police_district_input) > 0:
    subset_data2 = mapa[mapa['Police District'].isin(police_district_input)]
    
subset_data1 =subset_data2
neighborhood_input = st.sidebar.multiselect(
'Neighborhood',
subset_data2.groupby('Neighborhood').count().reset_index()['Neighborhood'].tolist())
if len(neighborhood_input) > 0:
    subset_data1 = subset_data2[subset_data2['Neighborhood'].isin(neighborhood_input)]

subset_data = subset_data1
incident_input = st.sidebar.multiselect(
'Incident Category',
subset_data1.groupby('Incident Category').count().reset_index()['Incident Category'].tolist())

if len(incident_input) > 0:
    subset_data = subset_data1[subset_data1['Incident Category'].isin(incident_input)]
    
    
subset_data5 = subset_data
incident_input = st.sidebar.multiselect(
'Report Type Description',
subset_data1.groupby('Report Type Description').count().reset_index()['Report Type Description'].tolist())

if len(incident_input) > 0:
    subset_data5 = subset_data1[subset_data1['Report Type Description'].isin(incident_input)]

subset_data4 = subset_data
incident_input = st.sidebar.multiselect(
'Incident Year',
subset_data1.groupby('Incident Year').count().reset_index()['Incident Year'].tolist())

if len(incident_input) > 0:
    subset_data4 = subset_data1[subset_data1['Incident Year'].isin(incident_input)]

subset_data4


st.markdown('It is important to mention that any police district can answer to any incident, the neighborhood in which it happened is not related to the police district.')




col1, col2 =  st.columns(2)


with col1:
    st.markdown('Crime locations in San Francisco')
    st.map(subset_data4)


with col2:
    st.markdown('Crimes occurred per day of the week')
    st.bar_chart(subset_data4['Day'].value_counts())
 
col3, col4 =  st.columns(2)


with col3:
    st.markdown('Crimes ocurred per date')
    st.line_chart(subset_data4['Day'].value_counts())


with col4:
    st.markdown('Crimes occurred per Year')
    st.bar_chart(subset_data4['Incident Year'].value_counts())


agree =st.button('Click to see Incident subcategories')

#####################

col5, col6=  st.columns(2)
with col5:
    st.markdown('Type of crimes commited')
    st.bar_chart(subset_data4['Incident Category']. value_counts())

with col6:     
    st.markdown('Crimes occurred per Neighborhood ')
    st.bar_chart(subset_data4['Neighborhood'].value_counts())
    


if agree:
    st.markdown('Subtype of crimes commited')
    st.bar_chart(subset_data4['Incident Category'].value_counts())
    

col7, col8=  st.columns(2)
with col7:
    st.markdown('Resolution status')
    fig1, ax1 = plt.subplots()
    labels = subset_data['Resolution'].unique()
    ax1.pie(subset_data['Resolution'].value_counts(), labels=labels, autopct="1.1f%%", startangle=20)
    st.pyplot(fig1)

with col8:
    st.markdown('Report Type Code')
    fig_pie, ax_pie = plt.subplots()
    labels_pie = subset_data4['Report Type Code'].unique()
    ax_pie.pie(subset_data4['Report Type Code'].value_counts(), labels=labels_pie, autopct="1.1f%%", startangle=20)
    st.pyplot(fig_pie)