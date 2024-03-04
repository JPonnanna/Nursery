# app.py

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to query data from the database
def query_data(tablename):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tablename}")
    data = cursor.fetchall()
    conn.close()
    return data

# Function to update data in the database
def update_data(tablename, id, value):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {tablename} SET value=? WHERE id=?", (value, id))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('gardener.html')

@app.route('/data/<tablename>')
def get_table_data(tablename):
    data = query_data(tablename)
    return jsonify(data)

@app.route('/update/<tablename>', methods=['POST'])
def update_table_data(tablename):
    id = request.form['id']
    value = request.form['value']
    update_data(tablename, id, value)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
