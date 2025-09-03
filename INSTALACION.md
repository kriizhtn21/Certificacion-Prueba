# 🚀 Instalación Rápida - Ideas Dashboard

## ⚡ Instalación en 5 Pasos

### 1. Prerrequisitos
- ✅ Python 3.8+ instalado
- ✅ MySQL 8.0+ instalado y ejecutándose
- ✅ MySQL Workbench (opcional, para gestión visual)

### 2. Configurar Base de Datos
```bash
# Abrir MySQL Workbench y ejecutar:
# Archivo: database_schema.sql
```

### 3. Instalar Dependencias
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar paquetes
pip install -r requirements.txt
```

### 4. Configurar Conexión
Editar `config.py` línea 12:
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://TU_USUARIO:TU_PASSWORD@localhost/ideas_dashboard'
```

### 5. Ejecutar Aplicación
```bash
# Inicializar base de datos (solo la primera vez)
python init_db.py

# Ejecutar aplicación
python run.py
```

## 🌐 Acceder a la Aplicación
- **URL**: http://localhost:5000
- **Usuarios de prueba**:
  - jane@example.com / password123
  - janice@example.com / password123
  - aleta@example.com / password123

## 🔧 Solución de Problemas

### Error de Conexión a MySQL
```bash
# Verificar que MySQL esté ejecutándose
# Windows: Servicios > MySQL80
# macOS: brew services start mysql
# Linux: sudo systemctl start mysql
```

### Error de Módulos Python
```bash
# Reinstalar dependencias
pip install --upgrade -r requirements.txt
```

### Error de Permisos de Base de Datos
```sql
-- En MySQL Workbench ejecutar:
CREATE USER 'tu_usuario'@'localhost' IDENTIFIED BY 'tu_password';
GRANT ALL PRIVILEGES ON ideas_dashboard.* TO 'tu_usuario'@'localhost';
FLUSH PRIVILEGES;
```

## 📁 Estructura del Proyecto
```
ideas-dashboard/
├── app.py              # Aplicación principal
├── config.py           # Configuraciones
├── models.py           # Modelos de base de datos
├── init_db.py          # Inicialización de BD
├── run.py              # Script de ejecución
├── requirements.txt    # Dependencias
├── database_schema.sql # Esquema de BD
├── routes/             # Rutas de la aplicación
├── templates/          # Plantillas HTML
└── static/             # Archivos CSS/JS
```

## ✅ Verificación de Instalación
1. ✅ MySQL ejecutándose
2. ✅ Base de datos `ideas_dashboard` creada
3. ✅ Dependencias Python instaladas
4. ✅ Aplicación ejecutándose en puerto 5000
5. ✅ Página de login/registro accesible

## 🆘 Soporte
Si tienes problemas:
1. Verificar logs de la aplicación
2. Verificar conexión a MySQL
3. Consultar con el instructor del curso
