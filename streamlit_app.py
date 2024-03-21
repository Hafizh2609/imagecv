import streamlit as st
from tablecv import extract_table
extracted_tables = extract_table(image_path="image_2024-03-20_18-49-05.png")

@st.experimental_memo
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


csv = convert_df(extracted_tables)
st.table(extracted_tables)
st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
