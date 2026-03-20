from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
def get_db():
    connection = sqlite3.connect("learning_python.db")
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/")
def home():
    return "Expense Tracker is running"

@app.route("/expenses")
def expenses():
   db = get_db()
   cursor = db.cursor()
   cursor.execute("SELECT * FROM expenses")
   expenses = cursor.fetchall()
   return render_template("expenses.html",expenses=expenses)

if __name__ == "__main__":
    app.run(debug=True)
