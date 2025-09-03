# 🚀 Guía de Despliegue en Railway

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
