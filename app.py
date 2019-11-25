#app.py 
import sqlite3
from flask import Flask, render_template, g

from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app

PATH = 'db/sqlite3'

# def open_connection():
#     connection = getattr(g, '_connection', None)
#     if connection == None:
#         connection = g._connection = sqlite3.connect(PATH)
#     connection.row_factory = sqlite3.Row
#     return connection

# def execute_sql(sql, values=(), commit=False, single=False):
#     connection = open_connection()
#     cursor = connection.execute(sql,values)
#     if commit == True:
#         results = connection.commit()
#     else:
#         results = cursor.fetchone() if single else cursor.fetchall()

#     cursor.close()
#     return results

# @app.teardown_appcontext
# def close_connection(exception):
#     connection = getattr(g, '_connection', None)
#     if connection is not None:
#         connection.close()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)