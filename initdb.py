import os
import psycopg2

conn_string = os.environ['CONNECTION_STRING']
conn = psycopg2.connect(conn_string)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS movies;')
cur.execute('CREATE TABLE movies (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'year INT NOT NULL,'
                                 'director varchar (50) NOT NULL,'
                                 'rating INT,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO movies (title, year, director, rating, review)'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Duna', 2021, 'Dennis Villeneuve', 4, 'Great adaption of a cassic sci-fi novel'))
cur.execute('INSERT INTO movies (title, year, director, rating, review)'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Elvis', 2022, 'Baz Luhrmann', 4, 'Hype stylized biopic of the King'))
cur.execute('INSERT INTO movies (title, year, director, rating, review)'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Machuca', 2004, 'Machua', 4, 'La película recibió muy buenas críticas luego de su estreno'))

conn.commit()

cur.close()
conn.close()