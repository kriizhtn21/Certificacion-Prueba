# Ideas Dashboard

Una aplicación web moderna para compartir y colaborar en ideas innovadoras, desarrollada con Flask y MySQL.

## Características

### Producto Mínimo Viable (MVP)
- ✅ **Autenticación con BCrypt**: Registro e inicio de sesión seguros
- ✅ **Programación Orientada a Objetos**: Modelos User, Idea y Team con relaciones
- ✅ **CRUD Completo**: Crear, leer, actualizar y eliminar ideas
- ✅ **Validaciones**: Todas las validaciones especificadas en el wireframe
- ✅ **Navegación**: Enrutamiento completo según especificaciones
- ✅ **Interfaz Responsiva**: Diseño minimalista y profesional

### Características de Extensión
- ✅ **Sistema de Equipos**: Los usuarios pueden unirse a equipos
- ✅ **Filtros por Equipo**: Ver ideas solo de miembros del mismo equipo
- ✅ **Validaciones Avanzadas**: Protección contra manipulación de URLs
- ✅ **Persistencia de Datos**: Guardado de datos en sesión para validaciones

## Tecnologías Utilizadas

- **Backend**: Python Flask
- **Base de Datos**: MySQL con SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Autenticación**: Flask-Bcrypt
- **Iconos**: Font Awesome 6

## Instalación

### Prerrequisitos
- Python 3.8+
- MySQL 8.0+
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd ideas-dashboard
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar MySQL**
   - Abrir MySQL Workbench
   - Ejecutar el script `database_schema.sql`
   - Verificar que la base de datos `ideas_dashboard` se haya creado

5. **Configurar la aplicación**
   - Editar `app.py` y actualizar la cadena de conexión a MySQL:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:contraseña@localhost/ideas_dashboard'
   ```

6. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

7. **Acceder a la aplicación**
   - Abrir navegador en `http://localhost:5000`

## Estructura del Proyecto

```
ideas-dashboard/
├── app.py                 # Aplicación principal Flask
├── models.py              # Modelos de base de datos
├── requirements.txt       # Dependencias de Python
├── database_schema.sql    # Esquema de base de datos
├── routes/                # Rutas de la aplicación
│   ├── __init__.py
│   ├── auth_routes.py     # Autenticación
│   ├── idea_routes.py     # Gestión de ideas
│   ├── user_routes.py     # Perfiles de usuario
│   └── team_routes.py     # Gestión de equipos
├── templates/             # Plantillas HTML
│   ├── base.html
│   ├── auth/
│   │   └── login_register.html
│   ├── ideas/
│   │   ├── dashboard.html
│   │   └── edit_idea.html
│   ├── users/
│   │   └── user_ideas.html
│   └── teams/
│       └── team_page.html
└── static/                # Archivos estáticos
    ├── css/
    │   └── style.css
    └── js/
        ├── main.js
        └── auth.js
```

## Funcionalidades

### Autenticación
- **Registro**: Validación completa de campos, verificación de email único
- **Inicio de Sesión**: Autenticación segura con BCrypt
- **Sesiones**: Control de acceso a páginas internas

### Gestión de Ideas
- **Crear Ideas**: Formulario con validación de longitud mínima
- **Ver Ideas**: Dashboard con todas las ideas y autores
- **Editar Ideas**: Solo el autor puede editar sus propias ideas
- **Eliminar Ideas**: Solo el autor puede eliminar sus propias ideas

### Perfiles de Usuario
- **Página de Usuario**: Ver todas las ideas de un usuario específico
- **Enlaces de Autor**: Navegación directa al perfil del autor

### Sistema de Equipos (Extensión)
- **Unirse a Equipos**: Seleccionar de equipos existentes
- **Crear Equipos**: Crear nuevos equipos únicos
- **Filtros**: Ver ideas solo de miembros del mismo equipo

## Validaciones Implementadas

### Registro
- Todos los campos son requeridos
- Nombre y apellido mínimo 2 caracteres
- Email válido y único
- Contraseña mínimo 8 caracteres
- Confirmación de contraseña debe coincidir

### Ideas
- Contenido requerido
- Mínimo 5 caracteres
- Solo el autor puede editar/eliminar

### Equipos
- Nombre del equipo requerido
- Nombre del equipo único
- Usuario solo puede pertenecer a un equipo

## Características de Diseño

- **Colores Minimalistas**: Paleta profesional con azules y grises
- **Responsive**: Adaptable a dispositivos móviles y desktop
- **Animaciones**: Transiciones suaves y efectos visuales
- **Accesibilidad**: Navegación por teclado y etiquetas ARIA
- **UX Moderna**: Interfaz intuitiva y fácil de usar

## Datos de Prueba

La base de datos incluye datos de ejemplo:
- **Usuarios**: jane@example.com, janice@example.com, aleta@example.com
- **Contraseña**: password123
- **Equipos**: Dev Project Ideas, Marketing Team, Design Team
- **Ideas**: Varias ideas de ejemplo para probar la funcionalidad

## Desarrollo

### Ejecutar en Modo Desarrollo
```bash
export FLASK_ENV=development  # En Windows: set FLASK_ENV=development
python app.py
```

### Estructura de Base de Datos
- **user**: Información de usuarios con encriptación de contraseñas
- **idea**: Ideas con relación a usuarios
- **team**: Equipos con relación a usuarios

## Licencia

Este proyecto es parte de una certificación académica.

## Contacto

Para preguntas sobre la implementación, consultar con el instructor del curso.
