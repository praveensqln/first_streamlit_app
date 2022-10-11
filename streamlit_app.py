
import streamlit 


streamlit.title('My Parents New Health Diner')

streamlit.header('Breakfast Menu')
streamlit.text( '	🌸:  Omega 3 and Blueberry Oatmeal')
streamlit.text( '🥗:	  Kale, Spinach and Rocket Smoothie')
streamlit.text( ' 🥚: Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑: Avacado tost')

streamlit.header(' 🍌  Build your own Fruit Smoothie 🍓 	🍉 ')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let us put a pick list here so they can be pick the fruit
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)
import requests
fruitvice_response = request.get("https://fruitvice.com/api/fruit/watermelon")
streamlit.text(fruitvice_response)
