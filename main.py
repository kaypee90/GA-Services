# author kaypee90

import psycopg3

def is_database_connected():
    try:
        # Replace with your actual database connection details
        conn = psycopg3.connect(
            host="postgres",
            database="postgresdb",
            user="postgres",
            password="postgres",
            port="5432"
        )

        with conn.cursor() as cursor:
            cursor.execute("SELECT  1;")
            result = cursor.fetchone()
            return result[0] ==  1

    except Exception as e:
        print(f"Error: {e}")
        return False

# Run the async functionx
connection_status = is_database_connected()
print(f"Database connected: {connection_status}")