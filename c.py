from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="nursery",
    password="xyz",
    database="users"
)
cursor = conn.cursor()

# Define a route to display data
@app.route('/')
def display_data():
    try:
        cursor.execute("SELECT * FROM names")
        data = cursor.fetchall()
        print("Fetched data:", data)  # Debugging statement
        return render_template('estbox.html', data=data)
    except Exception as e:
        print("Error fetching data:", e)  # Debugging statement
        return "An error occurred while fetching data."

if __name__ == '__main__':
    app.run(debug=True)
