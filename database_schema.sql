-- Esquema de base de datos para Ideas Dashboard
-- Ejecutar este script en MySQL Workbench

CREATE DATABASE IF NOT EXISTS ideas_dashboard;
USE ideas_dashboard;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    team_id INT NULL,
    INDEX idx_email (email),
    INDEX idx_team_id (team_id)
);

-- Tabla de equipos
CREATE TABLE IF NOT EXISTS team (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_name (name)
);

-- Tabla de ideas
CREATE TABLE IF NOT EXISTS idea (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    user_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_user_id (user_id),
    INDEX idx_created_at (created_at),
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);

-- Agregar foreign key para team_id después de crear la tabla team
ALTER TABLE user 
ADD CONSTRAINT fk_user_team 
FOREIGN KEY (team_id) REFERENCES team(id) ON DELETE SET NULL;

-- Insertar algunos datos de ejemplo
INSERT INTO team (name) VALUES 
('Dev Project Ideas'),
('Marketing Team'),
('Design Team');

-- Insertar usuarios de ejemplo (contraseñas: 'password123')
INSERT INTO user (first_name, last_name, email, password_hash, team_id) VALUES 
('Jane', 'Doe', 'jane@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8Kz8Kz2', 1),
('Janice', 'Smith', 'janice@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8Kz8Kz2', 1),
('Aleta', 'Johnson', 'aleta@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8Kz8Kz2', 2);

-- Insertar ideas de ejemplo
INSERT INTO idea (content, user_id) VALUES 
('¡Las cortadoras de césped a vapor son el próximo gran invento! Construyamos un prototipo.', 2),
('Es hora de crear una aplicación para dueños de mascotas que rastree su frecuencia cardíaca, movimiento y patrones de sueño', 1),
('¿Qué tal un sitio de comercio electrónico para intercambiar máquinas de arcade vintage y pinball?', 3),
('Podríamos construir una aplicación para encontrar gatos que permita a los usuarios publicar ubicaciones donde han visto un gato callejero', 3);
