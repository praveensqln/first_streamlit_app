
import streamlit 
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Health Diner')

streamlit.header('Breakfast Menu')
streamlit.text( '	🌸:  Omega 3 and Blueberry Oatmeal')
streamlit.text( '🥗:	  Kale, Spinach and Rocket Smoothie')
streamlit.text( ' 🥚: Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑: Avacado tost')

streamlit.header(' 🍌  Build your own Fruit Smoothie 🍓 	🍉 ')

# import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let us put a pick list here so they can be pick the fruit
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page

streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruitvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice )
    fruityvice_normalized = pandas.json_normalize(fruitvice_response.json())
    return fruityvice_normalized

streamlit.header("Fruitvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about ?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
          
except URLError as e:
       streamlit.error()
# streamlit.write('The user entered', fruit_choice)


#import requests



# streamlit.text(fruitvice_response.json())
# Formates data

#Display formated data

#import snowflake_connector
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * FROM fruit_load_list") 
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

streamlit.header("View Our Fruit List - Add Your Favourites!")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

#Add a button to load the fruit
if streamlit.button('Get Fruit List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_Data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    my_cnx.close()

#streamlit.stop()
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
        return "Thanks for adding "+ new_fruit
    
add_my_fruit = streamlit.text_input('What fruit would you like to add ?')
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
    my_cnx.close()

    #streamlit.write('Thanks for adding ', add_my_fruit)
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
