from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",  # Change this to your database server
    user="nursery",    # Change this to your database username
    password="xyz",    # Change this to your database password
    database="users"   # Change this to your database name
)

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        position = request.form['position']

        # SQL query to validate username, password, and position
        sql = "SELECT * FROM names WHERE username=%s AND password=%s AND position=%s"
        cursor.execute(sql, (username, password, position))
        result = cursor.fetchone()

        if result:
            if position == '1':
                return redirect(url_for('owner'))
            elif position == '2':
                return redirect(url_for('manager'))
            elif position == '3':
                return redirect(url_for('gardener'))
        else:
            # Invalid credentials
            return "Invalid username, password, or position."

    return render_template('index.html')

@app.route('/owner')
def owner():
    return render_template('owner.html')

@app.route('/manager')
def manager():
    return render_template('manager.html')

@app.route('/gardener')
def gardener():
    return render_template('gardener.html')

if __name__ == '__main__':
    app.run(debug=True)
