# server/routes/user_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from server.models import db, User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        user = User(username=username, password=password, role=role)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_routes.login'))
    return render_template('register.html')

@user_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            session['role'] = user.role
            return redirect(url_for('user_routes.profile', user_id=user.id))
        else:
            flash('Invalid credentials')
    return render_template('login.html')
