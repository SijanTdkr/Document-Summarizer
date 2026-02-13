# import mysql.connector
# from mysql.connector import Error

# def connect_to_mysql():
#     try:
#         # Establish the connection
#         connection = mysql.connector.connect(
#             host='127.0.0.1',       # Replace with your MySQL server address (e.g., 'localhost' or an IP)
#             user='root',            # Replace with your MySQL username
#             password='',    # Replace with your MySQL password
#             database='doc_summarizer_db'  # Replace with your database name
#         )
        
#         if connection.is_connected():
#             print("Successfully connected to MySQL database")

#             # Get server information
#             db_info = connection.get_server_info()
#             print(f"Server version: {db_info}")

#             # You can now interact with your MySQL database using the connection object.

#     except Error as e:
#         print(f"Error while connecting to MySQL: {e}")
#     finally:
#         # Close the connection if it's open
#         if connection.is_connected():
#             connection.close()
#             print("MySQL connection is closed")

# if __name__ == "__main__":
#     connect_to_mysql()


import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Replace with your database host
        user="root",  # Replace with your database username
        password="",  # Replace with your database password
        database="db_DocumentSummarizer"
    )
