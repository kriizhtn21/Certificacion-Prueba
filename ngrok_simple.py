"""
Script simple para usar ngrok y compartir la aplicación Flask
"""

import subprocess
import webbrowser
import time
import urllib.request
import json
import os

def check_ngrok_installed():
    """Verificar si ngrok está instalado"""
    try:
        result = subprocess.run(["ngrok", "version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ ngrok está instalado")
            return True
    except FileNotFoundError:
        pass
    
    print("❌ ngrok no está instalado")
    return False

def get_ngrok_url():
    """Obtener la URL pública de ngrok"""
    try:
        with urllib.request.urlopen("http://localhost:4040/api/tunnels") as response:
            data = json.loads(response.read().decode())
            if data['tunnels']:
                return data['tunnels'][0]['public_url']
    except:
        pass
    return None

def main():
    print("🚀 NGROK - Compartir tu aplicación Flask")
    print("=" * 50)
    
    # Verificar si ngrok está instalado
    if not check_ngrok_installed():
        print("\n📥 **INSTALAR NGROK:**")
        print("1. Ve a: https://ngrok.com/download")
        print("2. Descarga ngrok para Windows")
        print("3. Extrae el archivo ngrok.exe")
        print("4. Colócalo en una carpeta del PATH o en esta carpeta")
        print("5. Ejecuta este script nuevamente")
        
        input("\n⏸️  Presiona Enter después de instalar ngrok...")
        
        # Verificar nuevamente
        if not check_ngrok_installed():
            print("❌ ngrok aún no está instalado. Sigue las instrucciones anteriores.")
            return
    
    print("\n🌐 **INICIANDO NGROK...**")
    print("📝 Nota: ngrok creará un túnel público a tu aplicación local")
    
    # Verificar que la app esté ejecutándose
    print("\n⚠️  IMPORTANTE: Asegúrate de que tu aplicación Flask esté ejecutándose:")
    print("   python app.py")
    
    input("\n⏸️  Presiona Enter cuando tu aplicación esté ejecutándose...")
    
    # Iniciar ngrok
    print("\n🚀 Iniciando túnel ngrok...")
    ngrok_process = subprocess.Popen(["ngrok", "http", "5000"])
    
    # Esperar a que ngrok se inicie
    print("⏳ Esperando a que ngrok se inicie...")
    time.sleep(5)
    
    # Obtener la URL pública
    public_url = get_ngrok_url()
    
    if public_url:
        print(f"\n🎉 ¡Tu aplicación está disponible públicamente!")
        print(f"🔗 URL pública: {public_url}")
        print(f"📱 Comparte esta URL con cualquier persona en el mundo")
        print(f"🌍 No necesitan estar en tu red local")
        
        # Abrir en el navegador
        try:
            webbrowser.open(public_url)
            print("🌐 Abriendo en el navegador...")
        except:
            print("🌐 Abre manualmente la URL en tu navegador")
        
        print(f"\n⚠️  IMPORTANTE:")
        print(f"   - Mantén este terminal abierto")
        print(f"   - La URL cambiará si reinicias ngrok")
        print(f"   - Es solo para pruebas, no para producción")
        print(f"   - Tu aplicación Flask debe seguir ejecutándose")
        
        print(f"\n📊 **PANEL DE NGROK:**")
        print(f"   Ve a: http://localhost:4040 para ver estadísticas")
        
        input("\n⏸️  Presiona Enter para detener ngrok...")
        ngrok_process.terminate()
        print("🛑 ngrok detenido")
    else:
        print("❌ No se pudo obtener la URL de ngrok")
        print("🔧 Verifica que ngrok esté ejecutándose correctamente")
        print("🌐 Ve a: http://localhost:4040 para ver el estado")

if __name__ == "__main__":
    main()
