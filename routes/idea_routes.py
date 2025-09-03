from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from models import User, Idea, db
from functools import wraps

idea_routes = Blueprint('ideas', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes iniciar sesión para acceder a esta página', 'error')
            return redirect(url_for('auth.index'))
        return f(*args, **kwargs)
    return decorated_function

@idea_routes.route('/ideas')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    
    # Obtener todas las ideas
    ideas = Idea.query.order_by(Idea.created_at.desc()).all()
    
    return render_template('ideas/dashboard.html', user=user, ideas=ideas)

@idea_routes.route('/ideas/add', methods=['POST'])
@login_required
def add_idea():
    content = request.form.get('content', '').strip()
    
    # Validación
    if not content:
        flash('La idea es requerida', 'error')
        return redirect(url_for('ideas.dashboard'))
    
    if len(content) < 5:
        flash('La idea debe tener al menos 5 caracteres', 'error')
        return redirect(url_for('ideas.dashboard'))
    
    # Crear idea
    try:
        idea = Idea(
            content=content,
            user_id=session['user_id']
        )
        db.session.add(idea)
        db.session.commit()
        flash('¡Idea agregada exitosamente!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error al agregar la idea. Inténtalo de nuevo.', 'error')
    
    return redirect(url_for('ideas.dashboard'))

@idea_routes.route('/ideas/edit/<int:idea_id>')
@login_required
def edit_idea_form(idea_id):
    user = User.query.get(session['user_id'])
    idea = Idea.query.get_or_404(idea_id)
    
    # Verificar que el usuario sea el autor de la idea
    if idea.user_id != user.id:
        flash('No tienes permisos para editar esta idea', 'error')
        return redirect(url_for('ideas.dashboard'))
    
    return render_template('ideas/edit_idea.html', user=user, idea=idea)

@idea_routes.route('/ideas/update/<int:idea_id>', methods=['POST'])
@login_required
def update_idea(idea_id):
    user = User.query.get(session['user_id'])
    idea = Idea.query.get_or_404(idea_id)
    
    # Verificar que el usuario sea el autor de la idea
    if idea.user_id != user.id:
        flash('No tienes permisos para editar esta idea', 'error')
        return redirect(url_for('ideas.dashboard'))
    
    content = request.form.get('content', '').strip()
    
    # Validaciones
    if not content:
        flash('La idea es requerida', 'error')
        return redirect(url_for('ideas.edit_idea_form', idea_id=idea_id))
    
    if len(content) < 5:
        flash('La idea debe tener al menos 5 caracteres', 'error')
        return redirect(url_for('ideas.edit_idea_form', idea_id=idea_id))
    
    # Actualizar idea
    try:
        idea.content = content
        db.session.commit()
        flash('¡Idea actualizada exitosamente!', 'success')
        return redirect(url_for('ideas.dashboard'))
    except Exception as e:
        db.session.rollback()
        flash('Error al actualizar la idea. Inténtalo de nuevo.', 'error')
        return redirect(url_for('ideas.edit_idea_form', idea_id=idea_id))

@idea_routes.route('/ideas/delete/<int:idea_id>')
@login_required
def delete_idea(idea_id):
    user = User.query.get(session['user_id'])
    idea = Idea.query.get_or_404(idea_id)
    
    # Verificar que el usuario sea el autor de la idea
    if idea.user_id != user.id:
        flash('No tienes permisos para eliminar esta idea', 'error')
        return redirect(url_for('ideas.dashboard'))
    
    try:
        db.session.delete(idea)
        db.session.commit()
        flash('Idea eliminada exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error al eliminar la idea. Inténtalo de nuevo.', 'error')
    
    return redirect(url_for('ideas.dashboard'))
