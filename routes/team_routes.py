from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from models import User, Team, db
from functools import wraps

team_routes = Blueprint('teams', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes iniciar sesión para acceder a esta página', 'error')
            return redirect(url_for('auth.index'))
        return f(*args, **kwargs)
    return decorated_function

@team_routes.route('/teams/new')
@login_required
def team_page():
    user = User.query.get(session['user_id'])
    teams = Team.query.all()
    
    return render_template('teams/team_page.html', user=user, teams=teams)

@team_routes.route('/teams/join', methods=['POST'])
@login_required
def join_team():
    user = User.query.get(session['user_id'])
    team_id = request.form.get('team_id')
    
    if not team_id:
        flash('Debes seleccionar un equipo', 'error')
        return redirect(url_for('teams.team_page'))
    
    team = Team.query.get_or_404(team_id)
    
    try:
        user.team_id = team.id
        db.session.commit()
        flash(f'Te has unido al equipo "{team.name}" exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error al unirse al equipo. Inténtalo de nuevo.', 'error')
    
    return redirect(url_for('teams.team_page'))

@team_routes.route('/teams/create', methods=['POST'])
@login_required
def create_team():
    user = User.query.get(session['user_id'])
    team_name = request.form.get('team_name', '').strip()
    
    # Validaciones
    if not team_name:
        flash('El nombre del equipo es requerido', 'error')
        return redirect(url_for('teams.team_page'))
    
    # Verificar si el nombre del equipo ya existe
    existing_team = Team.query.filter_by(name=team_name).first()
    if existing_team:
        flash('Ya existe un equipo con este nombre', 'error')
        return redirect(url_for('teams.team_page'))
    
    try:
        # Crear equipo
        team = Team(name=team_name)
        db.session.add(team)
        db.session.flush()  # Para obtener el ID del equipo
        
        # Unir al usuario al equipo
        user.team_id = team.id
        db.session.commit()
        
        flash(f'Equipo "{team_name}" creado exitosamente y te has unido a él', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error al crear el equipo. Inténtalo de nuevo.', 'error')
    
    return redirect(url_for('teams.team_page'))
