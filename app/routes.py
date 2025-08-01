#Holds your URL routes, which tell Flask what to do when someone visits a page.
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

# Blueprint lets us separate routes from main file
main = Blueprint('main', __name__)

setup_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(setup_dir, "Database.db")
print("DB Path:", db_path)

# When someone visits the home page ('/'), show index.html
@main.route('/')
def home():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    msg = None
    msg_type = None

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        #Get user record
        cursor.execute("SELECT password FROM UsersTable WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result:
            stored_hashed_password = result[0]
            if check_password_hash(stored_hashed_password, password):
                msg = f"Welcome, {username}"
                msg_type = "server-msg"
                session['username'] = username # Store username in session
                return redirect(url_for('main.app_home'))
            else:
                msg = f"Invalid credentials, please try again!"
                msg_type = "error-msg"
        else: 
            msg = "Username not found."
            msg_type = "error-msg"

    return render_template('login_page.html', msg = msg, msg_type = msg_type)

@main.route('/register', methods=['GET', 'POST'])
def register():
    msg = None
    msg_type = None

    if request.method == 'POST':
        #Retrieve the values they submited in the form
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        #Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        #Check if username already exists
        cursor.execute("SELECT * FROM UsersTable WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            msg = "Username is already taken. Please choose another!"
            msg_type = "error-msg"

        else: 
            # If username is unique, insert the new user
            cursor.execute("INSERT INTO UsersTable (username, password) VALUES (?, ?)",(username, hashed_password))
            conn.commit()
            msg = f"Welcome, {username}! Your account has been created."
            msg_type = "server-msg"
        
        conn.close()

    return render_template('register_page.html', msg = msg, msg_type = msg_type)

@main.route('/app_home', methods=['GET', 'POST'])
def app_home():
    '''username = session.get('username')
    fav_number = None

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if request.method == "POST":
        new_fav_number = request.form['fav_number']
        
        #Check if already has a fav number
        cursor.execute("SELECT * FROM FavoriteNumber WHERE Username = ?", (username,))
        existing = cursor.fetchone()

        if existing:
            cursor.execute("UPDATE FavoriteNumber SET FavoriteNumber = ? WHERE Username = ?", (new_fav_number, username))
        else:
            cursor.execute("INSERT INTO FavoriteNumber (Username, FavoriteNumber) VALUES (?, ?)", (username, new_fav_number))

        conn.commit()
    
    #Get current favorite number
    cursor.execute("SELECT FavoriteNumber FROM FavoriteNumber WHERE Username = ?", (username,))
    row = cursor.fetchone()

    if row:
        fav_number = row[0]

    conn.close()'''


    return render_template('app_home.html')

@main.route('/add_expense', methods=['GET', 'POST'])
def add_expense():

    return render_template('add_expense.html')

@main.route('/add_income', methods=['GET', 'POST'])
def add_income():

    return render_template('add_income.html')

@main.route('/goals_page', methods=['GET', 'POST'])
def goals_page():

    return render_template('goals_page.html')

@main.route('/view_budget_sheet', methods=['GET', 'POST'])
def view_budget_sheet():
    
    return render_template('view_budget_sheet.html')