from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from models import User, db
import re

auth_routes = Blueprint('auth', __name__)

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@auth_routes.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('ideas.dashboard'))
    return render_template('auth/login_register.html')

@auth_routes.route('/register', methods=['POST'])
def register():
    # Obtener datos del formulario
    first_name = request.form.get('first_name', '').strip()
    last_name = request.form.get('last_name', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')
    
    # Validaciones
    errors = []
    
    # Todos los campos son requeridos
    if not first_name:
        errors.append('El nombre es requerido')
    elif len(first_name) < 2:
        errors.append('El nombre debe tener al menos 2 caracteres')
    
    if not last_name:
        errors.append('El apellido es requerido')
    elif len(last_name) < 2:
        errors.append('El apellido debe tener al menos 2 caracteres')
    
    if not email:
        errors.append('El email es requerido')
    elif not validate_email(email):
        errors.append('El email debe ser válido')
    elif User.query.filter_by(email=email).first():
        errors.append('Ya existe una cuenta con este email')
    
    if not password:
        errors.append('La contraseña es requerida')
    elif len(password) < 8:
        errors.append('La contraseña debe tener al menos 8 caracteres')
    
    if not confirm_password:
        errors.append('La confirmación de contraseña es requerida')
    elif password != confirm_password:
        errors.append('Las contraseñas no coinciden')
    
    if errors:
        for error in errors:
            flash(error, 'error')
        return redirect(url_for('auth.index'))
    
    # Crear usuario
    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        # NO iniciar sesión automáticamente
        # session['user_id'] = user.id
        flash(f'¡Registro exitoso! Tu cuenta ha sido creada correctamente. Ahora puedes iniciar sesión con tu email: {email}', 'success')
        return redirect(url_for('auth.index'))
    except Exception as e:
        db.session.rollback()
        flash('Error al crear la cuenta. Inténtalo de nuevo.', 'error')
        return redirect(url_for('auth.index'))

@auth_routes.route('/login', methods=['POST'])
def login():
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    
    # Validaciones
    if not email:
        flash('El email es requerido', 'error')
        return redirect(url_for('auth.index'))
    
    if not password:
        flash('La contraseña es requerida', 'error')
        return redirect(url_for('auth.index'))
    
    # Buscar usuario
    user = User.query.filter_by(email=email).first()
    
    if not user:
        flash('No existe una cuenta con este email', 'error')
        return redirect(url_for('auth.index'))
    
    if not user.check_password(password):
        flash('La contraseña es incorrecta', 'error')
        return redirect(url_for('auth.index'))
    
    # Login exitoso
    session['user_id'] = user.id
    flash(f'¡Bienvenido, {user.get_full_name()}!', 'success')
    return redirect(url_for('ideas.dashboard'))

@auth_routes.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión exitosamente', 'info')
    return redirect(url_for('auth.index'))
