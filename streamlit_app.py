import streamlit

streamlit.title('My Moms new Healthy Dinner')
streamlit.header(' Breakfast Favorites')
streamlit.text(' 🥣Bleuberry Oatmeal')
streamlit.text(' 🥗Spinach Smoothie')
streamlit.text(' 🐔Boiled Egg')
streamlit.text(' 🥑Avacado')

                
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
