from flask import Blueprint, render_template, session, flash, redirect, url_for
from models import User, Idea
from functools import wraps

user_routes = Blueprint('users', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes iniciar sesión para acceder a esta página', 'error')
            return redirect(url_for('auth.index'))
        return f(*args, **kwargs)
    return decorated_function

@user_routes.route('/users/<int:user_id>')
@login_required
def user_ideas(user_id):
    current_user = User.query.get(session['user_id'])
    target_user = User.query.get_or_404(user_id)
    
    # Obtener todas las ideas del usuario
    ideas = Idea.query.filter_by(user_id=user_id).order_by(Idea.created_at.desc()).all()
    
    return render_template('users/user_ideas.html', 
                         current_user=current_user, 
                         target_user=target_user, 
                         ideas=ideas)
