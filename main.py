from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
  conn_string = os.environ['CONNECTION_STRING']
  conn = psycopg2.connect(conn_string)
  return conn


@app.route('/')
def index():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('SELECT * FROM movies;')
  movies = cur.fetchall()
  response = ""
  for movie in movies:
    response += "<div>"
    response += "<h3>" + str(movie[0] )+ " - " + str(movie[1]) + "</h3>"
    response += "<i><p>(" + str(movie[2]) + ")</p></i>"
    response += "<i><p>Director: " + str(movie[3]) + "</p></i>"
    response += "<p>" + str(movie[5])+  "</p>"
    response += "<i><p>Rating: " + str(movie[4]) +" / 5</p></i>"
    response += "<i><p>Added: " + str(movie[6])+ "</p></i>"
    response += "</div>"

  cur.close()
  conn.close()
  return response
  
app.run(host='0.0.0.0', port=8080)



