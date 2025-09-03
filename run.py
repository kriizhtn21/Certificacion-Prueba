#!/usr/bin/env python3
"""
Script principal para ejecutar la aplicación Ideas Dashboard
"""

import os
import sys
from app import app, db

def check_database_connection():
    """Verificar conexión a la base de datos"""
    try:
        with app.app_context():
            db.engine.execute('SELECT 1')
        return True
    except Exception as e:
        print(f"❌ Error de conexión a la base de datos: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 Iniciando Ideas Dashboard...")
    
    # Verificar conexión a la base de datos
    if not check_database_connection():
        print("\n💡 Soluciones posibles:")
        print("1. Verificar que MySQL esté ejecutándose")
        print("2. Verificar las credenciales en app.py")
        print("3. Ejecutar el script de inicialización: python init_db.py")
        return
    
    print("✅ Conexión a la base de datos exitosa")
    
    # Crear tablas si no existen
    with app.app_context():
        db.create_all()
    
    print("✅ Tablas de base de datos verificadas")
    
    # Ejecutar la aplicación
    print("\n🌐 Iniciando servidor web...")
    print("📍 URL: http://localhost:5000")
    print("⏹️  Presiona Ctrl+C para detener el servidor")
    print("-" * 50)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido. ¡Hasta luego!")

if __name__ == "__main__":
    main()
