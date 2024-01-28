import mysql.connector
import streamlit as st

from langchain_experimental.sql import SQLDatabaseChain


@st.cache(allow_output_mutation=True)
def get_database_connection():
    # Establish MySQL database connection
    conn = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        passwd="",  # Provide your database password here
        db="mydb"
    )
    return conn


@st.cache
def view_all_data(conn):
    # Create a cursor
    c = conn.cursor()

    c.execute('SELECT * FROM insurance ORDER BY id ASC')
    data = c.fetchall()

    # Close the cursor
    c.close()

    return data


# Streamlit UI
st.title("View All Data")

# Fetch data and display
conn = get_database_connection()
data = view_all_data(conn)
st.write(data)

# Close the database connection when done
conn.close()
