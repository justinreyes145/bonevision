import sqlite3


def create_table():
    try:
        # Connecting to sqlite db
        conn = sqlite3.connect('patient_info.db')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS patients")

        # Creating table
        table = """ CREATE TABLE patients (
                    Test_ID INTEGER PRIMARY KEY,
                    Username CHAR(25),
                    Name CHAR(25),
                    Visit_Date DATE,
                    Birth_Date DATE,
                    Bone CHAR(20),
                    Fracture CHAR(10),
                    Image_Path CHAR(25),
                    Notes MEDIUMTEXT
                ); """
        cursor.execute(table)

        # Committing changes in the database and closing the connection
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)


def insert_one(username, name, visit_date, birth_date, bone, is_fractured, image_path, notes):
    try:
        # Connecting to sqlite db
        conn = sqlite3.connect('patient_info.db')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Inserting values with parametrized input to prevent SQL injection
        table = """ INSERT INTO patients
                    VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?); """
        cursor.execute(table, (username, name, visit_date, birth_date, bone, is_fractured, image_path, notes))
        last_id = cursor.lastrowid

        # Committing changes in the database and closing the connection
        conn.commit()
        conn.close()

        return last_id
    except sqlite3.Error as e:
        print(e)
        return -1


def update_img_path(test_id, image_path):
    try:
        # Connecting to sqlite db
        conn = sqlite3.connect('patient_info.db')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Inserting values with parametrized input to prevent SQL injection
        table = """ UPDATE patients SET Image_Path = ?
                    WHERE Test_ID = ?; """
        cursor.execute(table, (image_path, test_id))

        # Committing changes in the database and closing the connection
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)


def find_name(name, username):
    name = '%' + name + '%'
    try:
        # Connecting to sqlite db
        conn = sqlite3.connect('patient_info.db')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Selecting values with parametrized input to prevent SQL injection
        find = """ SELECT * FROM patients WHERE Name LIKE ? AND Username = ?"""
        data = cursor.execute(find, (name,username,))
        values = list(data)

        # Committing changes in the database and closing the connection
        conn.commit()
        conn.close()
        return values
    except sqlite3.Error as e:
        print(e)
        return None


# Run this once to create the db file and table
if __name__ == '__main__':
    # print(find_name('', 'cat'))
    create_table()
