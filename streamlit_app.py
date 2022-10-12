
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

fruit_choice = streamlit.text_input('What fruit would you like information about ?', 'kiwi')
streamlit.write('The user entered', fruit_choice)


import requests
fruitvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice )

streamlit.header("Fruitvice Fruit Advice!")
# streamlit.text(fruitvice_response.json())
# Formates data
fruityvice_normalized = pandas.json_normalize(fruitvice_response.json())
#Display formated data
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_aCCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * FROM fruit_load_list") 
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add ?)
streamlit.write('Thanks for adding ', add_my_fruit)
