import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#add title
st. title("Data Analysis Applications")
st.subheader("This is a simple data analysis application crated by Mohd Rashid")

#load data
#create a dropdown list to choose a dataset
dataset_options= ['iris', 'titanic','tips','diamonds' ]
selected_dataset = st.sidebar.selectbox('Seelct a dataset', dataset_options)

#load the selected dataset
if selected_dataset =='iris':
    df= sns.load_dataset('iris')
elif selected_dataset=='titanic':
    df=sns.load_dataset('titanic')
elif selected_dataset=='tips':
    df= sns. load_dataset('tips')
elif selected_dataset=='diamonds':
    df= sns. load_dataset('diamonds') 

#button to upload custom dataset
uploaded_file= st.sidebar.file_uploader("Upload a custom dataset", type= ['csv','xlsx'])

if uploaded_file is not None:
    #process the uploaded file
    df = pd.read_csv(uploaded_file) # assuming the upload file is in CSV format

#display the dataset
st.write(df)

#display the number of rows adn columns from the selected data
st.write('Number of rows: ',df.shape[0]) 
st.write('Number of columns:', df.shape[1])

#display the column names of selected data with their data types
st.write('Column names and Date Types:', df.dtypes)

#print the null values if those are >0
if df.isnull().sum().sum()>0:
    st.write('Null Values:',df.isnull().sum().sort_values(ascending=False))
else:
    st.write('No null values')

    #display the summary statistics of the selectd data
    st.write('Summary Statistics:', df.describe())

#select the spedific columns for X or Y Asis form the dataset and also select the type of the plot
# x_axis = st.sidebar.selectbox('Select X-axis', df.columns)
# y_axis = st.sidebar.selectbox('Select Y-axis', df.columns)
# plot_type= st.sidebar.selectbox('Select Plot Type', ['line','scatter','bar','hist','box','kde'])

#plot the data
# st.write("Chart/Plot")
# if plot_type=='line':
#     st.line_chart(df[[x_axis,y_axis]])
# elif plot_type=='scatter':
#      st.scatter_chart(df[[x_axis,y_axis]])
# elif plot_type=='bar':
#      st.bar_chart(df[[x_axis,y_axis]])
# elif plot_type=='hist':
#      df[x_axis].plot(kind='hist')
#      st.pyplot()
# elif plot_type=='box':
#      df[x_axis, y_axis].plot(kind='box')
#      st.pyplot()
# elif plot_type=='kde':
#      df[x_axis, y_axis].plot(kind='kde')
#      st.pyplot()


#create a pairplot
st.subheader("Pairplot")
#select the column to be used as hue in paiplot
hue_column= st.sidebar.selectbox('Select a column to be used as hue', df.columns)
st.pyplot(sns.pairplot(df, hue = hue_column))