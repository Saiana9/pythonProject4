import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
import altair as alt

# header
st.header('''Анализ заработной платы по видам экономической деятельности: образование, строительство и здравоохранение''')

# Displaying an image
image = Image.open('data/3677111.jpg')
st.image(image)

# load data
PATH_DATA = "data/df.csv"

@st.cache_data
def load_data(path):
    """Load data from path"""
    data = pd.read_csv(path)
    return data
df = load_data(PATH_DATA)
if st.checkbox('Показать данные'):
   st.write(df)


st.line_chart(df)

def main():
    df = load_data(PATH_DATA)
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    if page == "Homepage":
        st.header("This is your data explorer.")
        st.write("Please select a page on the left.")
        st.write(df)
    elif page == "Exploration":
        st.title("Data Exploration")
        x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)
        y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=4)
        visualize_data(df, x_axis, y_axis)


def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color='Origin',
        tooltip=['Строительство реальная зп', 'Строительство реальная зп', 'Строительство реальная зп', 'Инфляция']
    ).interactive()

    st.write(graph)

if __name__ == "__main__":
    main()
