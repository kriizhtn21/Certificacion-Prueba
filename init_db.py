#!/usr/bin/env python3
"""
Script de inicialización de la base de datos para Ideas Dashboard
"""

from app import app, db, bcrypt
from models import User, Idea, Team
from datetime import datetime

def init_database():
    """Inicializar la base de datos con tablas y datos de ejemplo"""
    
    with app.app_context():
        # Crear todas las tablas
        print("Creando tablas de la base de datos...")
        db.create_all()
        
        # Verificar si ya existen datos
        if User.query.first():
            print("La base de datos ya contiene datos. Saltando inserción de datos de ejemplo.")
            return
        
        print("Insertando datos de ejemplo...")
        
        # Crear equipos
        teams = [
            Team(name="Dev Project Ideas"),
            Team(name="Marketing Team"),
            Team(name="Design Team")
        ]
        
        for team in teams:
            db.session.add(team)
        
        db.session.flush()  # Para obtener los IDs de los equipos
        
        # Crear usuarios con contraseñas encriptadas
        users = [
            User(
                first_name="Jane",
                last_name="Doe",
                email="jane@example.com",
                team_id=teams[0].id
            ),
            User(
                first_name="Janice",
                last_name="Smith",
                email="janice@example.com",
                team_id=teams[0].id
            ),
            User(
                first_name="Aleta",
                last_name="Johnson",
                email="aleta@example.com",
                team_id=teams[1].id
            )
        ]
        
        # Establecer contraseñas
        password = "password123"
        for user in users:
            user.set_password(password)
            db.session.add(user)
        
        db.session.flush()  # Para obtener los IDs de los usuarios
        
        # Crear ideas de ejemplo
        ideas = [
            Idea(
                content="¡Las cortadoras de césped a vapor son el próximo gran invento! Construyamos un prototipo.",
                user_id=users[1].id  # Janice
            ),
            Idea(
                content="Es hora de crear una aplicación para dueños de mascotas que rastree su frecuencia cardíaca, movimiento y patrones de sueño",
                user_id=users[0].id  # Jane
            ),
            Idea(
                content="¿Qué tal un sitio de comercio electrónico para intercambiar máquinas de arcade vintage y pinball?",
                user_id=users[2].id  # Aleta
            ),
            Idea(
                content="Podríamos construir una aplicación para encontrar gatos que permita a los usuarios publicar ubicaciones donde han visto un gato callejero",
                user_id=users[2].id  # Aleta
            )
        ]
        
        for idea in ideas:
            db.session.add(idea)
        
        # Confirmar todos los cambios
        db.session.commit()
        
        print("✅ Base de datos inicializada exitosamente!")
        print("\nDatos de ejemplo creados:")
        print("👥 Usuarios:")
        for user in users:
            print(f"   - {user.get_full_name()} ({user.email}) - Contraseña: {password}")
        print("\n🏢 Equipos:")
        for team in teams:
            print(f"   - {team.name}")
        print("\n💡 Ideas:")
        for idea in ideas:
            print(f"   - {idea.content[:50]}... (por {idea.author.first_name})")

def reset_database():
    """Eliminar todas las tablas y recrearlas"""
    
    with app.app_context():
        print("⚠️  Eliminando todas las tablas...")
        db.drop_all()
        print("✅ Tablas eliminadas.")
        init_database()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--reset":
        reset_database()
    else:
        init_database()
    
    print("\n🚀 Para ejecutar la aplicación:")
    print("   python app.py")
    print("\n🌐 Luego abrir en el navegador:")
    print("   http://localhost:5000")
