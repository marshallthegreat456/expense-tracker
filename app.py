from flask import Flask
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

   result = ""
   for expense in expenses:
       result += f"ID: {expense['id']} | Name {expense['name']} | Amount {expense['amount']}<br>"

   return result if result else "No expenses found"

if __name__ == "__main__":
    app.run(debug=True)