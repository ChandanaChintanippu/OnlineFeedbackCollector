from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'Chandu2811'  # Change this to a secure secret in production


# Function to initialize DB and create Feedback table
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS Feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        rating INTEGER,
        comments TEXT,
        date_submitted TEXT
    )
    ''')
    conn.close()


# Home Page with Feedback Form
@app.route('/')
def home():
    return render_template('index.html')


# Handle Feedback Form Submission
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    rating = request.form['rating']
    comments = request.form['comments']
    date_submitted = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO Feedback (name, email, rating, comments, date_submitted) VALUES (?, ?, ?, ?, ?)",
                 (name, email, rating, comments, date_submitted))
    conn.commit()
    conn.close()

    return redirect('/')


# Admin Dashboard (Login Required)
@app.route('/admin-dashboard')
def admin_dashboard():
    if not session.get('admin'):
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Feedback")
    feedbacks = cursor.fetchall()

    cursor.execute("SELECT COUNT(*), AVG(rating) FROM Feedback")
    total, avg_rating = cursor.fetchone()
    conn.close()

    return render_template('admin.html', feedbacks=feedbacks, total=total, avg_rating=round(avg_rating or 0, 2))


# Admin Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin123':
            session['admin'] = True
            return redirect('/admin-dashboard')
        else:
            return "Invalid credentials. Try again."
    return render_template('login.html')


# Admin Logout
@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')


# Optional REST API Endpoint to get feedback as JSON
@app.route('/api/feedback')
def api_feedback():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Feedback")
    rows = cursor.fetchall()
    conn.close()

    feedback_list = [dict(row) for row in rows]
    return json.dumps(feedback_list, indent=2)

@app.route('/export')
def export():
    if not session.get('admin'):
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Feedback")
    feedbacks = cursor.fetchall()
    conn.close()

    import csv
    from io import StringIO
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Name', 'Email', 'Rating', 'Comments', 'Date'])

    for row in feedbacks:
        writer.writerow(row)

    output.seek(0)
    return (output.read(), 
            {'Content-Type': 'text/csv', 'Content-Disposition': 'attachment; filename="feedback.csv"'})

# Run the Flask app
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
