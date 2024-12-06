from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.security import generate_password_hash
from .models import User
from . import db

bp = Blueprint('main', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(email=email).first():
            flash('Этот email уже зарегистрирован.')
            return redirect('/register')

        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Вы успешно зарегистрировались!')
        return redirect('/register')
    
    return render_template('register.html')
