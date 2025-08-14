# --------------------------------------------
# Flask Final Project: CRUD + Forms + Layout
# --------------------------------------------

from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# ------------------ DATABASE CONNECTION ------------------
def get_db_connection():
    conn = sqlite3.connect("final.db")     # Connect to database
    conn.row_factory = sqlite3.Row         # Access rows by column name
    return conn

# ------------------ INITIAL DATABASE SETUP ------------------
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)  # Create table if it doesn't exist
    conn.commit()
    conn.close()

# ------------------ READ & CREATE ------------------
@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:  # Input validation
            users = conn.execute("SELECT * FROM users").fetchall()
            conn.close()
            return render_template("index.html", users=users, error="Fill all fields!")

        # Insert new user
        conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()

    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("index.html", users=users)

# ------------------ UPDATE ------------------
@app.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit(user_id):
    conn = get_db_connection()

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        conn.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, user_id))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    user = conn.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    conn.close()
    return render_template("edit.html", user=user)

# ------------------ DELETE ------------------
@app.route("/delete/<int:user_id>")
def delete(user_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

# ------------------ RUN APP ------------------
if __name__ == "__main__":
    init_db()               # Ensure database and table exist
    app.run(debug=True)     # Run server in debug mode






#how to run:
#python app.py


#acess:
#http://127.0.0.1:5000/ → Form + list of users
#Add, Edit, Delete users in one interface
#Works on mobile and desktop (Bootstrap layout)


#Example Browser Output:
#Home page with navbar, form, table of users
#Edit page with pre-filled form
#Delete confirmation pop-up


# --------------------------------------------
# SUMMARY:
# - Integrated Flask CRUD, forms, SQLite, and Bootstrap layout
# - Created reusable layout template for all pages
# - Input validation with basic error messages
# - Added responsive design for mobile and desktop
#
# TIPS:
# - Always validate user inputs before database operations
# - Use Bootstrap classes for consistent UI and responsiveness
# - Confirm deletion actions to prevent data loss
# - Keep templates clean and separate layout from content
# - Organize code with functions for database handling
# --------------------------------------------
