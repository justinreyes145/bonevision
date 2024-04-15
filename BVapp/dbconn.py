import sqlite3

try:
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('patient_info.db')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Write a query and execute it with cursor
    query = 'select sqlite_version();'
    cursor.execute(query)

    # Fetch and output result
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))

    # Close the cursor
    cursor.close()
# Handle errors
except sqlite3.Error as error:
    print('Error occurred - ', error)
# Close DB Connection irrespective of success or failure
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')

def testCreate():
    # Connecting to sqlite
    # connection object
    connection_obj = sqlite3.connect('patient_info.db')

    # cursor object
    cursor_obj = connection_obj.cursor()

    # Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS patients")

    # Creating table
    table = """ CREATE TABLE patients (
                First_Name CHAR(25) NOT NULL,
                Last_Name CHAR(25),
                Date DATE
            ); """

    cursor_obj.execute(table)

    print("Table is Ready")

    # Close the connection
    connection_obj.close()

def insert():
    # Connecting to sqlite
    conn = sqlite3.connect('patient_info.db')

    # Creating a cursor object using the
    # cursor() method
    cursor = conn.cursor()

    # Creating table
    table = """ CREATE TABLE patients (
                First_Name CHAR(25) NOT NULL,
                Last_Name CHAR(25),
                Date DATE
            ); """
    # cursor.execute(table)

    # Queries to INSERT records.
    # cursor.execute('''INSERT INTO patients VALUES ('Cheol', 'Reyes', '1111-11-11')''')

    # Display data inserted
    print("Data Inserted in the table: ")
    data = cursor.execute('''SELECT * FROM patients WHERE Last_Name = "Reyes" AND First_Name = "Justin"''')
    for row in data:
        print(row)

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()

# testCreate()
insert()