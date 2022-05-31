import streamlit
import pandas

streamlit.title('Feed me, Seymour!')  

#streamlit.header(':-) A Header of Note')
#streamlit.text('ConTEXTual text, eh?')

my_fruit_list = pandas.read("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#streamlit.text('Show and tell, Pandas')
#streamlit.dataframe(my_fruit_list)
   
