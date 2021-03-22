import streamlit as st
import pandas as pd
name = st.text_input("User Name","Yashaswini")
File = st.file_uploader("Upload File",type = 'csv')
click = st.button("Submit")
if (click == True):
    st.write("Output 1 - Display top 5 rows of the dataframe")
    df = pd.read_csv("C:\\Users\\saisr\\Desktop\\Temp2\\iris\\iris.csv")
    st.write(df.head())

    st.write("Output 2 - Display the Scatter plot between PetalLengthCm and SepallengthCm")
    import matplotlib.pyplot as plt
    fig = plt.figure()
    plt.scatter(df["petal.length"],df["sepal.length"])
    plt.xlabel('Petal Length Cm')
    plt.ylabel('Sepal Length Cm')
    st.write(fig)
