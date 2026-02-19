import mysql.connector

# 1. Establish the connection
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",      # Your MySQL username (usually 'root')
        password="Mysql@savin9", # Your MySQL password
        database="my_first_db"
    )
    
    cursor = db.cursor()
    print("Successfully connected to the database!")

    # 2. Create a simple table for "Contacts"
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), phone VARCHAR(20))")

    # 3. Insert a new record (using %s to prevent SQL Injection)
    sql = "INSERT INTO contacts (name, phone) VALUES (%s, %s)"
    val = ("John Doe", "555-0199")
    
    cursor.execute(sql, val)
    db.commit() # This "saves" the changes to the database

    cursor.execute("SELECT DATABASE()")
    print("Python is currently using the database",cursor.fetchone())
    print(f"{cursor.rowcount} record inserted.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("Connection closed.")