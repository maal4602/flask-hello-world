import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://cspb3308_lab10_db_user:PlUaHbOmC7ShaAVxj9fG1pxMHAdTM7Y8@dpg-cgi9711r8t1g7lvn4ghg-a/cspb3308_lab10_db")
    conn.close()
    return "Database Connection Successful"