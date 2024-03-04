# app.py

from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__,static_url_path='/static')

# Function to query data from the database
def query_data(box_id):
    # Connect to MySQL database
    conn = mysql.connector.connect(
    host="localhost",  # Change this to your database server
    user="nursery",    # Change this to your database username
    password="xyz",    # Change this to your database password
    database="users"   # Change this to your database name
)
    cursor = conn.cursor()
    # Example query based on box_id, modify as per your database schema
    cursor.execute("SELECT * FROM users ")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    return render_template('c.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    # Get the box_id from the frontend
    box_id = request.json['box_id']
    # Query data from the database based on box_id
    data = query_data(box_id)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
