"""
Script para configurar PythonAnywhere y desplegar la aplicación Flask
"""

import os

def create_pythonanywhere_files():
    """Crear archivos necesarios para PythonAnywhere"""
    
    # requirements.txt
    requirements = """Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Bcrypt==1.0.1
PyMySQL==1.1.0
python-dotenv==1.0.0
"""
    
    with open("requirements.txt", "w") as f:
        f.write(requirements)
    
    # wsgi.py
    wsgi_content = '''import sys
import os

# Añadir el directorio del proyecto al path
path = '/home/tu_usuario/mi_proyecto'
if path not in sys.path:
    sys.path.append(path)

from app import app as application

if __name__ == "__main__":
    application.run()
'''
    
    with open("wsgi.py", "w") as f:
        f.write(wsgi_content)
    
    print("✅ Archivos de PythonAnywhere creados exitosamente")

def create_deployment_guide():
    """Crear guía de despliegue para PythonAnywhere"""
    
    guide = """# 🐍 Guía de Despliegue en PythonAnywhere

## 📋 **Pasos para Desplegar:**

### 1. **Crear Cuenta en PythonAnywhere**
- Ve a https://www.pythonanywhere.com
- Crea una cuenta gratuita
- Confirma tu email

### 2. **Subir tu Código**
```bash
# Opción 1: Git (recomendado)
git init
git add .
git commit -m "Initial commit"
git push origin main

# Opción 2: Subir archivos manualmente
# Usa el panel de archivos de PythonAnywhere
```

### 3. **Configurar Base de Datos**
- Ve a la pestaña "Databases"
- Crea una base de datos MySQL
- Anota las credenciales

### 4. **Instalar Dependencias**
```bash
# En la consola de PythonAnywhere
pip3.10 install --user -r requirements.txt
```

### 5. **Configurar Variables de Entorno**
```bash
# En la consola
export FLASK_ENV=production
export SECRET_KEY="tu_clave_secreta_muy_segura_aqui"
export DATABASE_URL="mysql+pymysql://usuario:password@host:puerto/database"
```

### 6. **Configurar la Aplicación Web**
- Ve a la pestaña "Web"
- Crea una nueva aplicación web
- Selecciona "Flask"
- Usa el archivo `wsgi.py`
- Configura el dominio

### 7. **Configurar el Dominio**
- Tu aplicación estará en: `tu_usuario.pythonanywhere.com`
- Puedes configurar un dominio personalizado

## ✅ **Ventajas de PythonAnywhere:**
- ✅ Gratis para proyectos pequeños
- ✅ Muy fácil de usar
- ✅ Base de datos MySQL incluida
- ✅ SSL automático
- ✅ Consola web integrada
- ✅ Perfecto para principiantes

## 🔗 **Enlaces Útiles:**
- PythonAnywhere: https://www.pythonanywhere.com
- Documentación: https://help.pythonanywhere.com
- Dashboard: https://www.pythonanywhere.com/user/tu_usuario/

## ⚠️ **Limitaciones del Plan Gratuito:**
- Solo 3 meses de uso
- CPU limitado
- Tráfico limitado
- Solo 1 aplicación web
"""
    
    with open("GUIA_PYTHONANYWHERE.md", "w", encoding="utf-8") as f:
        f.write(guide)
    
    print("✅ Guía de PythonAnywhere creada: GUIA_PYTHONANYWHERE.md")

def main():
    print("🐍 Configurando PythonAnywhere para desplegar tu aplicación Flask")
    print("=" * 60)
    
    create_pythonanywhere_files()
    create_deployment_guide()
    
    print("\n🎉 ¡Configuración completada!")
    print("📖 Lee GUIA_PYTHONANYWHERE.md para los pasos de despliegue")
    print("🌐 Tu aplicación estará disponible 24/7 en internet")

if __name__ == "__main__":
    main()
