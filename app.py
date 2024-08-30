from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
import pdfkit
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB setup
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restaurant_app_1'
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('menu'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Use 'pbkdf2:sha256' for password hashing
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        mongo.db.users.insert_one({'username': username, 'password': hashed_password})
        flash('Registration successful', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        selected_items = request.form.getlist('items')
        session['order'] = selected_items
        return redirect(url_for('order_summary'))

    # Fetch menu items from the database
    menu_items_cursor = mongo.db.menu_items.find()
    menu_items = {item['name']: item['price'] for item in menu_items_cursor}
    
    return render_template('menu.html', menu=menu_items)

@app.route('/order_summary', methods=['GET', 'POST'])
def order_summary():
    order_items = session.get('order', [])
    menu_items_cursor = mongo.db.menu_items.find()
    menu_items = {item['name']: item['price'] for item in menu_items_cursor}
    
    total = sum(menu_items.get(item, 0) for item in order_items)
    if request.method == 'POST':
        return generate_pdf(order_items, total, menu_items)
    return render_template('order_summary.html', items=order_items, total=total, menu=menu_items)

def generate_pdf(order_items, total, menu_items):
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'   # Adjust the path based on your installation
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

    html = render_template('bill_template.html', items=order_items, total=total, menu=menu_items)
    pdf_path = f'static/bills/bill_{ObjectId()}.pdf'
    pdfkit.from_string(html, pdf_path, configuration=config)
    return redirect(url_for('static', filename=f'bills/{os.path.basename(pdf_path)}'))

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
