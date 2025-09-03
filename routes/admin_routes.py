#!/usr/bin/env python3
"""
Rutas de administración para Ideas Dashboard
"""

from flask import Blueprint, render_template, session, redirect, url_for, flash
from models import User, Team, Idea

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/test-users')
def test_users():
    """Mostrar usuarios de prueba disponibles"""
    
    # Obtener todos los usuarios de prueba
    test_users = User.query.all()
    teams = Team.query.all()
    
    return render_template('admin/test_users.html', 
                         users=test_users, 
                         teams=teams)
