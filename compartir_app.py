"""
Script principal para compartir tu aplicación Flask
"""

import os
import sys
import subprocess
import webbrowser
import time

def print_banner():
    """Mostrar banner de bienvenida"""
    print("=" * 60)
    print("🌐 COMPARTIR APLICACIÓN FLASK")
    print("=" * 60)
    print("Elige cómo quieres compartir tu aplicación:")
    print()

def show_menu():
    """Mostrar menú de opciones"""
    print("📋 **OPCIONES DISPONIBLES:**")
    print()
    print("1. 🌐 Red Local (misma WiFi)")
    print("   - Fácil y rápido")
    print("   - Solo funciona en la misma red")
    print()
    print("2. 🚀 ngrok (Acceso instantáneo)")
    print("   - URL pública temporal")
    print("   - Acceso desde cualquier lugar")
    print("   - Requiere mantener tu computadora encendida")
    print()
    print("3. 🚂 Railway (Servidor en la nube)")
    print("   - Disponible 24/7")
    print("   - Base de datos incluida")
    print("   - Perfecto para producción")
    print()
    print("4. 🐍 PythonAnywhere (Más simple)")
    print("   - Muy fácil de usar")
    print("   - Perfecto para principiantes")
    print("   - Plan gratuito limitado")
    print()
    print("5. 📖 Ver instrucciones completas")
    print("6. ❌ Salir")
    print()

def get_user_choice():
    """Obtener elección del usuario"""
    while True:
        try:
            choice = input("🔢 Elige una opción (1-6): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6']:
                return choice
            else:
                print("❌ Opción inválida. Elige un número del 1 al 6.")
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            sys.exit(0)

def run_local_network():
    """Configurar red local"""
    print("\n🌐 **CONFIGURANDO RED LOCAL**")
    print("=" * 40)
    
    # Verificar que la app esté ejecutándose
    print("✅ Tu aplicación ya está configurada para red local")
    print("🔗 URL local: http://192.168.1.100:5000")
    print()
    print("📱 **Para que otros accedan:**")
    print("   1. Asegúrate de que estén en la misma WiFi")
    print("   2. Comparte la URL: http://192.168.1.100:5000")
    print("   3. Si no funciona, ejecuta como administrador:")
    print("      netsh advfirewall firewall add rule name=\"Flask App\" dir=in action=allow protocol=TCP localport=5000")
    
    input("\n⏸️  Presiona Enter para continuar...")

def run_ngrok():
    """Configurar ngrok"""
    print("\n🚀 **CONFIGURANDO NGROK**")
    print("=" * 40)
    
    try:
        # Ejecutar el script simple de ngrok
        subprocess.run([sys.executable, "ngrok_simple.py"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Error ejecutando ngrok_simple.py")
        print("🔧 Ejecuta manualmente: python ngrok_simple.py")
    except FileNotFoundError:
        print("❌ Archivo ngrok_simple.py no encontrado")
        print("🔧 Asegúrate de que el archivo existe en el directorio actual")
    except KeyboardInterrupt:
        print("\n⏸️  Operación cancelada por el usuario")

def run_railway():
    """Configurar Railway"""
    print("\n🚂 **CONFIGURANDO RAILWAY**")
    print("=" * 40)
    
    try:
        # Ejecutar el script de Railway
        subprocess.run([sys.executable, "railway_setup.py"], check=True)
        print("\n📖 **Siguiente paso:**")
        print("   Lee GUIA_RAILWAY.md para completar el despliegue")
    except subprocess.CalledProcessError:
        print("❌ Error ejecutando railway_setup.py")
        print("🔧 Ejecuta manualmente: python railway_setup.py")
    except FileNotFoundError:
        print("❌ Archivo railway_setup.py no encontrado")
        print("🔧 Asegúrate de que el archivo existe en el directorio actual")

def run_pythonanywhere():
    """Configurar PythonAnywhere"""
    print("\n🐍 **CONFIGURANDO PYTHONANYWHERE**")
    print("=" * 40)
    
    try:
        # Ejecutar el script de PythonAnywhere
        subprocess.run([sys.executable, "pythonanywhere_setup.py"], check=True)
        print("\n📖 **Siguiente paso:**")
        print("   Lee GUIA_PYTHONANYWHERE.md para completar el despliegue")
    except subprocess.CalledProcessError:
        print("❌ Error ejecutando pythonanywhere_setup.py")
        print("🔧 Ejecuta manualmente: python pythonanywhere_setup.py")
    except FileNotFoundError:
        print("❌ Archivo pythonanywhere_setup.py no encontrado")
        print("🔧 Asegúrate de que el archivo existe en el directorio actual")

def show_instructions():
    """Mostrar instrucciones completas"""
    print("\n📖 **INSTRUCCIONES COMPLETAS**")
    print("=" * 40)
    
    if os.path.exists("INSTRUCCIONES_COMPARTIR.md"):
        print("📄 Abriendo INSTRUCCIONES_COMPARTIR.md...")
        try:
            # Intentar abrir con el editor por defecto
            if sys.platform == "win32":
                os.startfile("INSTRUCCIONES_COMPARTIR.md")
            elif sys.platform == "darwin":
                subprocess.run(["open", "INSTRUCCIONES_COMPARTIR.md"])
            else:
                subprocess.run(["xdg-open", "INSTRUCCIONES_COMPARTIR.md"])
        except:
            print("📝 Lee el archivo INSTRUCCIONES_COMPARTIR.md manualmente")
    else:
        print("❌ Archivo INSTRUCCIONES_COMPARTIR.md no encontrado")
    
    input("\n⏸️  Presiona Enter para continuar...")

def main():
    """Función principal"""
    while True:
        print_banner()
        show_menu()
        
        choice = get_user_choice()
        
        if choice == '1':
            run_local_network()
        elif choice == '2':
            run_ngrok()
        elif choice == '3':
            run_railway()
        elif choice == '4':
            run_pythonanywhere()
        elif choice == '5':
            show_instructions()
        elif choice == '6':
            print("\n👋 ¡Hasta luego!")
            break
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
