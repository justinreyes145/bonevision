import sqlite3


def create_table():
    try:
        # Connecting to sqlite db
        conn = sqlite3.connect('patient_info.db')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Creating table
        table = """ CREATE TABLE patients (
                    First_Name CHAR(25) NOT NULL,
                    Last_Name CHAR(25),
                    Visit_Date DATE,
                    Birth_Date DATE,
                    Fracture CHAR(3),
                    Image_Path CHAR(25),
                    Notes MEDIUMTEXT
                ); """
        cursor.execute(table)

        # Committing changes in the database and closing the connection
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def insert_one(first_name, last_name, visit_date, birth_date, is_fractured, image_path, notes):
    try:
        # Connecting to sqlite db
        conn = sqlite3.connect('patient_info.db')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Inserting values with parametrized input to prevent SQL injection
        table = """ INSERT INTO patient_info.patients
                    VALUES (?); """
        cursor.execute(table, (first_name, last_name, visit_date, birth_date, is_fractured, image_path, notes))

        # Committing changes in the database and closing the connection
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def find_first_name(first_name):
    try:
        # Connecting to sqlite db
        conn = sqlite3.connect('patient_info.db')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Selecting values with parametrized input to prevent SQL injection
        find = """ SELECT * FROM patients WHERE first_name = ?"""
        data = cursor.execute(find, (first_name,))
        for row in data:
            print(row)

    # Committing changes in the database and closing the connection
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


# Run this once to create the db file and table
# create_table()
