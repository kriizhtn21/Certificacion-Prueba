"""
Script para configurar Railway y desplegar la aplicación Flask
"""

import os
import subprocess
import json

def create_railway_files():
    """Crear archivos necesarios para Railway"""
    
    # requirements.txt
    requirements = """Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Bcrypt==1.0.1
PyMySQL==1.1.0
python-dotenv==1.0.0
gunicorn==21.2.0
"""
    
    with open("requirements.txt", "w") as f:
        f.write(requirements)
    
    # Procfile
    procfile = "web: gunicorn app:app"
    with open("Procfile", "w") as f:
        f.write(procfile)
    
    # railway.json
    railway_config = {
        "build": {
            "builder": "NIXPACKS"
        },
        "deploy": {
            "startCommand": "gunicorn app:app",
            "restartPolicyType": "ON_FAILURE",
            "restartPolicyMaxRetries": 10
        }
    }
    
    with open("railway.json", "w") as f:
        json.dump(railway_config, f, indent=2)
    
    # .env.example
    env_example = """# Configuración para Railway
FLASK_ENV=production
SECRET_KEY=tu_clave_secreta_muy_segura_aqui
DATABASE_URL=mysql+pymysql://usuario:password@host:puerto/database

# Variables de entorno de Railway
RAILWAY_STATIC_URL=
RAILWAY_PUBLIC_DOMAIN=
"""
    
    with open(".env.example", "w") as f:
        f.write(env_example)
    
    print("✅ Archivos de Railway creados exitosamente")

def create_deployment_guide():
    """Crear guía de despliegue"""
    
    guide = """# 🚀 Guía de Despliegue en Railway

## 📋 **Pasos para Desplegar:**

### 1. **Preparar el Proyecto**
```bash
# Los archivos ya están creados:
# - requirements.txt
# - Procfile  
# - railway.json
# - .env.example
```

### 2. **Instalar Railway CLI**
```bash
# Opción 1: npm
npm install -g @railway/cli

# Opción 2: PowerShell
iwr -useb https://railway.app/install.ps1 | iex
```

### 3. **Configurar Base de Datos**
- Ve a https://railway.app
- Crea una cuenta gratuita
- Crea un nuevo proyecto
- Añade un servicio MySQL
- Copia las credenciales de conexión

### 4. **Desplegar la Aplicación**
```bash
# Iniciar sesión
railway login

# Inicializar proyecto
railway init

# Configurar variables de entorno
railway variables set DATABASE_URL="mysql+pymysql://usuario:password@host:puerto/database"
railway variables set SECRET_KEY="tu_clave_secreta_muy_segura_aqui"
railway variables set FLASK_ENV="production"

# Desplegar
railway up
```

### 5. **Configurar Dominio**
- Railway te dará una URL automática
- Puedes configurar un dominio personalizado
- La aplicación estará disponible 24/7

## ✅ **Ventajas de Railway:**
- ✅ Gratis para proyectos pequeños
- ✅ Despliegue automático desde GitHub
- ✅ Base de datos MySQL incluida
- ✅ SSL automático
- ✅ Escalado automático
- ✅ Logs en tiempo real

## 🔗 **Enlaces Útiles:**
- Railway: https://railway.app
- Documentación: https://docs.railway.app
- Dashboard: https://railway.app/dashboard
"""
    
    with open("GUIA_RAILWAY.md", "w", encoding="utf-8") as f:
        f.write(guide)
    
    print("✅ Guía de Railway creada: GUIA_RAILWAY.md")

def main():
    print("🚀 Configurando Railway para desplegar tu aplicación Flask")
    print("=" * 60)
    
    create_railway_files()
    create_deployment_guide()
    
    print("\n🎉 ¡Configuración completada!")
    print("📖 Lee GUIA_RAILWAY.md para los pasos de despliegue")
    print("🌐 Tu aplicación estará disponible 24/7 en internet")

if __name__ == "__main__":
    main()
